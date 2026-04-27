# -*- coding: utf-8 -*-
Feature: University Website Search
  As a prospective student
  I want to search for academic programs on university websites
  So that I can find information about careers and programs offered

  Background:
    Given I have a web browser open

  Scenario Outline: Search for academic programs on university websites via Google
    Given I am on the Google homepage
    When I search for "<University>" on Google
    And I click the first result link for "<Domain>"
    Then I should be on the "<University Name>" website with title containing "<Title Keyword>"
    When I search for "<Search Term>" within the university website
    Then the results should contain information about "<Expected Content>"

    Examples: Universities and their program search terms
      | University        | Domain         | University Name | Title Keyword | Search Term        | Expected Content        |
      | iteso             | iteso.mx       | ITESO           | ITESO         | carreras           | carreras                |
      | udg               | udg.mx         | UDG             | UDG           | carreras           | carreras                |
      | tec monterrey     | tec.mx         | Tec de Monterrey| Tec           | programas          | programas               |
