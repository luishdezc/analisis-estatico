# -*- coding: utf-8 -*-
# pylint: disable=import-error,no-name-in-module

"""
Environment configuration for Behave tests.
Handles browser setup and teardown.

Requirements:
  - Google Chrome installed on your machine.
  - A matching ChromeDriver binary available on PATH.
    Download from: https://googlechromelabs.github.io/chrome-for-testing/
    Or install via package manager:
      macOS:  brew install --cask chromedriver
      Linux:  sudo apt install chromium-driver
      Windows: place chromedriver.exe somewhere on your PATH
"""

import os

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium import webdriver


def get_driver():
    """
    Creates and returns a configured Chrome WebDriver.
    ChromeDriver is resolved from the system PATH automatically.

    To point to a specific binary instead, set the CHROMEDRIVER_PATH env var:
        export CHROMEDRIVER_PATH=/path/to/chromedriver
        behave
    """
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    chromedriver_path = os.environ.get("CHROMEDRIVER_PATH")
    service = (
        Service(executable_path=chromedriver_path) if chromedriver_path else Service()
    )

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver


# pylint: disable=unused-argument
def before_scenario(context, scenario):
    """
    Opens a fresh browser before each scenario.
    """
    context.driver = get_driver()


# pylint: disable=unused-argument
def after_scenario(context, scenario):
    """
    Closes the browser after each scenario.
    """
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()
