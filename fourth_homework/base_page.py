#!/usr/bin/python
# -*- coding: UTF-8 -*-


import logging
from fourth_homework.locators import Locators as locators


def login_input(driver, login):
    """
    Input email address to login field
    :param driver: browser web driver
    :param login: user email address
    """
    locator = locators.email_input_locator
    logging.debug("Try to find login input field with locator {}".format(*locator))
    driver.find_element(*locator).send_keys(login)


def password_input(driver, password):
    """
    Input password to password field
    :param driver: browser web driver
    :param password: user password
    """
    locator = locators.password_input_locator
    logging.debug("Try to find password input field with locator {}".format(*locator))
    driver.find_element(*locator).send_keys(password)


def accept_button_click(driver):
    """
    Click on accept button
    :param driver: browser web driver
    """
    locator = locators.login_button_locator
    logging.debug("Try to click on accept button with locator {}".format(*locator))
    driver.find_element(*locator).click()


def get_warning_message(driver):
    """
    Parse warning object to get warning text
    :param driver: browser web driver
    :return: text - error message
    """
    locator = locators.warning_locator
    response = driver.find_element(*locator)
    error_text = response.text
    return error_text
