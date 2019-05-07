#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.locators import Locators as locators
from fives_homework.base_page import BasePage


class AdminLoginPage(BasePage):
    @staticmethod
    def login_input(driver, login):
        """
        Input email address to login field
        :param driver: browser web driver
        :param login: user email address
        """
        BasePage.send_keys_to_object(driver, locator=locators.login_input_locator, some_keys=login)

    @staticmethod
    def password_input(driver, password):
        """
        Input password to password field
        :param driver: browser web driver
        :param password: user password
        """
        BasePage.send_keys_to_object(driver, locator=locators.password_input_locator, some_keys=password)

    @staticmethod
    def accept_button_click(driver):
        """
        Click on accept button
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=locators.login_button_locator)
