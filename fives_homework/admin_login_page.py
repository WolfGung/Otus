#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.locators import Locators as locators
from fives_homework.base_page import BasePage


class AdminLoginPage(BasePage):
    def __init__(self):
        self.login_field_locator = locators.login_input_locator
        self.password_field_locator = locators.password_input_locator
        self.accept_button_locator = locators.login_button_locator

    def login_input(self, driver, login):
        """
        Input email address to login field
        :param driver: browser web driver
        :param login: user email address
        """
        self.send_keys_to_object(driver=driver, locator=self.login_field_locator, some_keys=login)

    def password_input(self, driver, password):
        """
        Input password to password field
        :param driver: browser web driver
        :param password: user password
        """
        self.send_keys_to_object(*driver, *self.password_field_locator, some_keys=password)

    def accept_button_click(self, driver):
        """
        Click on accept button
        :param driver: browser web driver
        """
        self.click_on_object(*driver, *self.accept_button_locator)
