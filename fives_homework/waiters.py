#!/usr/bin/python
# -*- coding: UTF-8 -*-


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging


def _wait_for_element(driver, locator, delay=5):
    """
    Waiting for element by locator
    :param driver: browser webdriver
    :param locator: locator of element that we want to wait
    """
    try:
        WebDriverWait(driver, int(delay)).until(EC.presence_of_element_located(locator))
    except(NoSuchElementException, TimeoutException):
        logging.error("There are no visible element in delay {}".format(delay))
