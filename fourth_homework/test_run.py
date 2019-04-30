#!/usr/bin/python
# -*- coding: UTF-8 -*-


import logging
from fourth_homework.base_page import login_input, password_input
from fourth_homework.base_page import accept_button_click, get_warning_message


def test001(start_browser):
    """
    Test type - positive
    Login with valid parameters
    :param start_browser: browser run
    """
    driver = start_browser
    login_input(driver, login="opencart@localhost.ru")
    password_input(driver, password="elephant")
    accept_button_click(driver)
    current_url = driver.current_url
    success_login_url = "http://192.168.102.98/opencart/index.php?route=account/account"
    logging.debug("Current web url is {}".format(current_url))
    assert driver.current_url == success_login_url


def test002(start_browser):
    """
    Test type - positive
    Login with valid parameters. E-Mail Address in uppercase.
    :param start_browser: browser run
    """
    driver = start_browser
    login_input(driver, login="OPENCART@LOCALHOST.ru")
    password_input(driver, password="elephant")
    accept_button_click(driver)
    current_url = driver.current_url
    success_login_url = "http://192.168.102.98/opencart/index.php?route=account/account"
    logging.debug("Current web url is {}".format(current_url))
    assert driver.current_url == success_login_url


def test003(start_browser):
    """
    Test type - negative
    Login with valid parameters. Password in uppercase.
    :param start_browser: browser run
    """
    driver = start_browser
    login_input(driver, login="opencart@localhost.ru")
    password_input(driver, password="ELEPHANT")
    accept_button_click(driver)
    current_url = driver.current_url
    error_text = get_warning_message(driver)
    correct_error = "Warning: No match for E-Mail Address and/or Password."
    logging.debug("Current web url is {}".format(current_url))
    logging.debug("Error text is {}".format(error_text))
    assert correct_error == error_text


def test004(start_browser):
    """
    Test type - negative
    Login with invalid E-Mail Address
    :param start_browser: browser run
    """
    driver = start_browser
    login_input(driver, login="opencart@wronglogin.ru")
    password_input(driver, password="elephant")
    accept_button_click(driver)
    current_url = driver.current_url
    error_text = get_warning_message(driver)
    correct_error =  "Warning: No match for E-Mail Address and/or Password."
    logging.debug("Current web url is {}".format(current_url))
    logging.debug("Error text is {}".format(error_text))
    assert correct_error == error_text


def test005(start_browser):
    """
    Test type - negative
    Login with invalid password
    :param start_browser:  browser run
    """
    driver = start_browser
    login_input(driver, login="opencart@localhost.ru")
    password_input(driver, password="wrongpassword")
    accept_button_click(driver)
    current_url = driver.current_url
    error_text = get_warning_message(driver)
    correct_error = "Warning: No match for E-Mail Address and/or Password."
    logging.debug("Current web url is {}".format(current_url))
    logging.debug("Error text is {}".format(error_text))
    assert correct_error == error_text


def test006(start_browser):
    """
    Test type - negative
    Login with invalid password and E-Mail Address
    :param start_browser:  browser run
    """
    driver = start_browser
    login_input(driver, login="opencart@wronglogin.ru")
    password_input(driver, password="wrongpassword")
    accept_button_click(driver)
    current_url = driver.current_url
    error_text = get_warning_message(driver)
    correct_error = "Warning: No match for E-Mail Address and/or Password."
    logging.debug("Current web url is {}".format(current_url))
    logging.debug("Error text is {}".format(error_text))
    assert correct_error == error_text


def test007(start_browser):
    """
    Test type - positive
    Login with valid parameters. Have numbers in login
    :param start_browser: browser run
    """
    driver = start_browser
    login_input(driver, login="1111@1111.ru")
    password_input(driver, password="elephant")
    accept_button_click(driver)
    current_url = driver.current_url
    success_login_url = "http://192.168.102.98/opencart/index.php?route=account/account"
    logging.debug("Current web url is {}".format(current_url))
    assert driver.current_url == success_login_url


def test008(start_browser):
    """
    Test type = positive
    Login with valid parameters. Have numbers in password
    :param start_browser: browser run
    """
    driver = start_browser
    login_input(driver, login="support@localhost.ru")
    password_input(driver, password="1111111")
    accept_button_click(driver)
    current_url = driver.current_url
    success_login_url = "http://192.168.102.98/opencart/index.php?route=account/account"
    logging.debug("Current web url is {}".format(current_url))
    assert driver.current_url == success_login_url


def test009(start_browser):
    """
    Test type = negative
    Login with NONE E-Mail Address
    :param start_browser: browser run
    """
    driver = start_browser
    password_input(driver, password="elephant")
    accept_button_click(driver)
    current_url = driver.current_url
    error_text = get_warning_message(driver)
    correct_error = "Warning: Your account has exceeded allowed " \
                    "number of login attempts. Please try again in 1 hour."
    logging.debug("Current web url is {}".format(current_url))
    logging.debug("Error text is {}".format(error_text))
    assert correct_error == error_text


def test010(start_browser):
    """
    Test type = negative
    Login with NONE password
    :param start_browser: browser run
    """
    driver = start_browser
    login_input(driver, login="opencart@localhost.ru")
    accept_button_click(driver)
    current_url = driver.current_url
    error_text = get_warning_message(driver)
    correct_error = "Warning: No match for E-Mail Address and/or Password."
    logging.debug("Current web url is {}".format(current_url))
    logging.debug("Error text is {}".format(error_text))
    assert correct_error == error_text
