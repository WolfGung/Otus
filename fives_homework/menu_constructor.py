#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.locators import Locators as locators
from fives_homework.base_page import BasePage
import logging


class MenuConstructor(BasePage):
    @staticmethod
    def drug_computer_drop_components(driver):
        """
        In the menu constructor drug computer menu and drop it to components
        :param driver: browser web driver
        """
        BasePage.drug_and_drop_element(driver, source_locator=locators.computer_menu_locator,
                                       target_locator=locators.components_menu_locator)

    @staticmethod
    def get_all_custom_menu_elements(driver):
        """
        Getting all elements in custom menu DOM
        :param driver: browser web driver
        :return: web elements
        """
        elements = driver.find_elements(locators.custom_constructor_menu)
        return elements

    @staticmethod
    def check_computer_element(driver):
        """
        Checking that 'computer' element placed on the 24 item place
        :param driver: browser web driver
        """
        element_24 = driver.find_element(locators.custom_menu_item_24_locator)
        text_attribute = element_24.text
        all_names = text_attribute.partition(" ")
        name = all_names[0]
        if name != "Компьютеры":
            raise AttributeError("There are no element with name:{} on 24 element position".format(name))
        else:
            logging.info("Element with name:{} on 24 element position".format(name))
