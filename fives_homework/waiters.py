#!/usr/bin/python
# -*- coding: UTF-8 -*-


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging


def _wait_for_element(driver, locator, delay=5):
    """
    Waiting for element visible by locator
    :param driver: browser web driver
    :param locator: locator of element that we want to wait
    :param delay: maximal time that we waiting till element came visible
    """
    try:
        WebDriverWait(driver, int(delay)).until(EC.presence_of_element_located(locator))
    except(NoSuchElementException, TimeoutException):
        driver.save_screenshot("./wait_for_element_screenshot")
        logging.error("There are no visible element in delay {}".format(delay))


def _wait_for_element_not(driver, locator, delay=5):
    """
    Waiting for element invisible by locator
    :param driver: browser web driver
    :param locator: locator of element that we want to wait
    :param delay: maximal time that we waiting till element came invisible
    """
    try:
        WebDriverWait(driver, int(delay)).until_not(EC.presence_of_element_located(locator))
    except(NoSuchElementException, TimeoutException):
        driver.save_screenshot("./not_wait_for_element_screenshot.png")
        logging.error("There are visible element with locator:{}".format(locator))


def _wait_for_alert(driver, alert_message, delay=5):
    """
    Waiting for alert
    :param driver: browser web driver
    :param alert_message: message in the alert window
    :param delay: maximal time that we waiting alert
    """
    try:
        WebDriverWait(driver, int(delay)).until(EC.alert_is_present(), alert_message)
    except(NoSuchElementException, TimeoutException):
        driver.save_screenshot("./alert_screenshot.png")
        logging.error("There are alert with message:{}".format(alert_message))
