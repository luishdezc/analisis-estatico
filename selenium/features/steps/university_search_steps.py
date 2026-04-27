# -*- coding: utf-8 -*-
# pylint: disable=import-error,no-name-in-module,not-callable,unused-import

"""
Step definitions for University Website Search BDD tests.
"""

import time

from behave import given, then, when
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DEFAULT_WAIT = 12


def wait_for(driver, condition, timeout=DEFAULT_WAIT):
    """
    Waits for an ExpectedCondition with a configurable timeout.
    """
    return WebDriverWait(driver, timeout).until(condition)


def accept_cookies_if_present(driver):
    """
    Dismisses cookie/consent banners that may block interaction.
    """
    selectors = [
        (By.XPATH, "//button[contains(., 'Aceptar')]"),
        (By.XPATH, "//button[contains(., 'Accept')]"),
        (By.ID, "L2AGLb"),
    ]
    for by, value in selectors:
        try:
            btn = driver.find_element(by, value)
            btn.click()
            time.sleep(1)
            return
        except NoSuchElementException:
            pass


def open_search_if_hidden(driver):
    """
    Some sites hide search behind an icon
    """
    try:
        btn = driver.find_element(
            By.CSS_SELECTOR,
            "button[aria-label*='search' i], button[aria-label*='buscar' i]",
        )
        btn.click()
        time.sleep(1)
    except NoSuchElementException:
        pass


def get_keywords(term):
    """
    Synonyms to make validation flexible
    """
    mapping = {
        "carreras": ["carreras", "programas", "licenciaturas", "degrees"],
        "licenciaturas": ["licenciaturas", "carreras", "programas"],
        "programas": ["programas", "programs", "degrees"],
    }
    return mapping.get(term.lower(), [term.lower()])


@given("I have a web browser open")  # pylint: disable=not-callable
def browser_ready(context):
    """
    Verifies that the browser driver exists (created in environment.py).
    """
    assert context.driver is not None


@given("I am on the Google homepage")  # pylint: disable=not-callable
def open_google(context):
    """
    Navigates to Google and accepts any consent banners.
    """
    context.driver.get("https://www.google.com")
    accept_cookies_if_present(context.driver)


@when('I search for "{query}" on Google')  # pylint: disable=not-callable
def search_on_google(context, query):
    """
    Types a query into the Google search box and submits it.
    """
    wait_for(context.driver, EC.presence_of_element_located((By.NAME, "q")))
    box = context.driver.find_element(By.NAME, "q")
    box.clear()
    box.send_keys(query)
    box.send_keys(Keys.RETURN)

    wait_for(context.driver, EC.presence_of_element_located((By.ID, "search")))


@when('I click the first result link for "{domain}"')  # pylint: disable=not-callable
def click_first_result(context, domain):
    """
    Finds the first organic Google result that contains *domain* in its URL
    and clicks it, then waits for the target page to load.
    """
    driver = context.driver

    wait_for(driver, EC.presence_of_element_located((By.CSS_SELECTOR, "#search a")))

    links = driver.find_elements(By.CSS_SELECTOR, "#search a[href]")

    for link in links:
        href = link.get_attribute("href") or ""
        if domain.lower() in href.lower():
            driver.get(href)
            break
    else:
        raise AssertionError(f"No result found for domain: {domain}")

    wait_for(driver, EC.presence_of_element_located((By.TAG_NAME, "body")))
    accept_cookies_if_present(driver)


@when(
    'I search for "{term}" within the university website'
)  # pylint: disable=not-callable
def search_term_on_university(context, term):
    """
    Searches for an arbitrary term on the currently open university site.
    """
    driver = context.driver
    open_search_if_hidden(driver)

    selectors = [
        "input[type='search']",
        "input[name='s']",
        "input[name='q']",
        "input[placeholder*='buscar' i]",
        "input[placeholder*='search' i]",
    ]

    search_input = None
    for sel in selectors:
        elements = driver.find_elements(By.CSS_SELECTOR, sel)
        if elements:
            search_input = elements[0]
            break

    if not search_input:
        base = driver.current_url.split("?")[0].rstrip("/")
        driver.get(f"{base}?s={term}")
    else:
        try:
            search_input.clear()
            search_input.send_keys(term)
            search_input.send_keys(Keys.RETURN)
        except Exception:  # pylint: disable=broad-exception-caught
            base = driver.current_url.split("?")[0]
            driver.get(f"{base}?s={term}")

    wait_for(driver, EC.presence_of_element_located((By.TAG_NAME, "body")))

    context.search_term = term


@then(
    'I should be on the "{university_name}" website with title containing "{keyword}"'
)  # pylint: disable=not-callable
def verify_university(context, university_name, keyword):
    """
    Asserts the current page belongs to the expected university by checking
    that the page title or URL contains the given keyword.
    """
    driver = context.driver

    url = driver.current_url.lower()
    title = driver.title.lower()

    assert (
        keyword.lower() in url or keyword.lower() in title
    ), f"Wrong site:\nURL: {driver.current_url}\nTitle: {driver.title}"

    print(f"\nVerified {university_name} → {driver.title}")


@then(
    'the results should contain information about "{expected_content}"'
)  # pylint: disable=not-callable
def verify_results(context, expected_content):
    """
    Checks that the page body contains content related to the expected term.
    """
    driver = context.driver

    if "cloudflare" in driver.title.lower():
        raise AssertionError("Blocked by Cloudflare (bot detected)")

    keywords = get_keywords(expected_content)

    page_text = driver.page_source.lower()

    matches = sum(1 for k in keywords if k in page_text)

    assert matches > 0, (
        f"No relevant content found.\n"
        f"Keywords: {keywords}\n"
        f"URL: {driver.current_url}\n"
        f"Title: {driver.title}"
    )

    print(f"\nValid content detected using keywords: {keywords}")
