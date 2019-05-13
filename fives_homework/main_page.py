#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.locators import Locators as locators
from fives_homework.base_page import BasePage


class MainPage(BasePage):
    @staticmethod
    def message_close_button_click(driver):
        """
        Click on close button of the message
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=locators.message_close_button_locator)

    @staticmethod
    def open_product_catalog(driver):
        """
        Open product catalog combobox
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=locators.product_catalog_locator)

    @staticmethod
    def click_product_button(driver):
        """
        Click on product button in the catalog
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=locators.product_button_locator)

    @staticmethod
    def click_downloads_button(driver):
        """
        Click on downloads button in the catalog
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locator=locators.downloads_menu_products_locator)
