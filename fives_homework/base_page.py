#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.waiters import _wait_for_element
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep


class BasePage:
    @staticmethod
    def send_keys_to_object(driver, locator, some_keys):
        """
        Send keys to the object
        :param locator: object locator
        :param driver: browser web driver
        :param some_keys: keys we want to send
        """
        _wait_for_element(driver, locator)
        driver.find_element(*locator).send_keys(some_keys)

    @staticmethod
    def click_on_object(driver, locator):
        """
        Click on object by locator
        :param driver: browser web driver
        :param locator: object locator
        """
        _wait_for_element(driver, locator)
        driver.find_element(*locator).click()

    @staticmethod
    def click_on_first_object_from_many(driver, locator, attribute, attribute_value):
        """
        Find and click on object from many objects by it attribute value
        :param driver: browser web driver
        :param locator: object locator
        :param attribute: object attribute
        :param attribute_value: object attribute value
        """
        _wait_for_element(driver, locator)
        buttons = driver.find_elements(*locator)
        for button in buttons:
            data = button.get_attribute(str(attribute))
            if data == attribute_value:
                button.click()
                break
            else:
                continue

    @staticmethod
    def click_on_all_object_from_many(driver, locator, attribute, attribute_value):
        """
        Find and click on object from many objects by it attribute value
        :param driver: browser web driver
        :param locator: object locator
        :param attribute: object attribute
        :param attribute_value: object attribute value
        """
        _wait_for_element(driver, locator)
        buttons = driver.find_elements(*locator)
        for button in buttons:
            data = button.get_attribute(str(attribute))
            if data == attribute_value:
                button.click()
            else:
                continue

    @staticmethod
    def clear_object(driver, locator):
        """
        Clear and object field
        :param driver: browser web driver
        :param locator: object locator
        """
        _wait_for_element(driver, locator)
        driver.find_element(*locator).clear()

    @staticmethod
    def alert_accept_click(driver):
        """
        Click accept on message
        :param driver: browser web driver
        """
        alert_obj = driver.switch_to.alert
        alert_obj.accept()

    @staticmethod
    def click_and_hold(driver, locator, timeout=2):
        """
        Click on element by mouse 1 and release it when timeout ends
        :param driver: browser web driver
        :param locator: object locator
        :param timeout: mouse release timeout
        """
        element = driver.find_element(locator)
        action = ActionChains(driver).click_and_hold(element)
        sleep(timeout)
        action.release()
        action.perform()

    @staticmethod
    def select_from_the_combobox_by_text(driver, locator, text):
        """
        Choose element from the combobox by text and click on it
        :param driver: browser web driver
        :param locator: object locator
        :param text: text of the element we want to click
        """
        select = Select(driver.find_element(locator))
        select.select_by_visible_text(text)

    @staticmethod
    def drug_and_drop_element(driver, source_locator, target_locator):
        """
        Drug an element and drop it to other element
        :param driver: browser web driver
        :param source_locator: locator of source element
        :param target_locator: locator of drop target element
        """
        source_element = driver.find_element(source_locator)
        target_element = driver.find_element(target_locator)
        action = ActionChains(driver).drag_and_drop(source_element, target_element)
        action.perform()
