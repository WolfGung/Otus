#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.locators import Locators as locators
from fives_homework.base_page import BasePage


class MainPage(BasePage):
    def __init__(self):
        self.message_close_button_locator = locators.message_close_button_locator
        self.product_catalog_locator = locators.product_catalog_locator
        self.product_button_catalog = locators.product_button_locator

    def message_close_button_click(self, driver):
        """
        Click on close button of the message
        :param driver: browser web driver
        """
        self.click_on_object(driver, locator=self.message_close_button_locator)

    def open_product_catalog(self, driver):
        """
        Open product catalog combobox
        :param driver: browser web driver
        """
        self.click_on_object(driver, locator=self.product_catalog_locator)

    def click_product_button(self, driver):
        """
        Click on product button in the catalog
        :param driver: browser web driver
        """
        self.click_on_object(driver, locator=self.product_button_catalog)






