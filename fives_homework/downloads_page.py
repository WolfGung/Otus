#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.locators import Locators as locators
from fives_homework.waiters import _wait_for_element, _wait_for_alert
from fives_homework.base_page import BasePage
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium.common.exceptions import NoSuchElementException
import logging


class DownloadsPage(BasePage):
    @staticmethod
    def click_add_new_file(driver):
        """
        Click on add new file button
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locators.add_new_downloads_file_locator)

    @staticmethod
    def input_download_file_name(driver, name):
        """
        Input file name to the Download Name field
        :param driver: browser web driver
        :param name: name for file that we will download
        """
        BasePage.send_keys_to_object(driver, locators.download_name_field_locator, some_keys=name)

    @staticmethod
    def download_file(driver, file_url):
        """
        Download file
        :param file_url: full url to downloadable file
        :param driver: browser web driver
        """
        _wait_for_element(driver, locators.file_upload_button_locator, delay=3)
        driver.find_element(*locators.file_upload_button_locator).click()
        keyboard = Controller()
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        driver.find_element(*locators.file_download_dynamic_locator).send_keys(file_url)
        alert_message = "Your file was successfully uploaded!"
        _wait_for_alert(driver, alert_message, delay=3)
        BasePage.alert_accept_click(driver)
        BasePage.click_on_object(driver, locators.save_downloaded_file)

    @staticmethod
    def check_downloaded_file(driver, file_name):
        """
        Check that file has been added
        :param driver: browser web driver
        :param file_name: name of downloaded file
        """
        try:
            driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(file_name))
        except NoSuchElementException:
            logging.error("There are no files with name:{}".format(file_name))

    @staticmethod
    def select_downloaded_file(driver):
        """
        Select first file checkbox
        :param driver: browser web driver
        """
        BasePage.click_on_first_object_from_many(driver,
                                                 locators.check_box_type_locator,
                                                 attribute="name",
                                                 attribute_value="selected[]")

    @staticmethod
    def delete_selected_file(driver):
        """
        Delete file that was selected by checkbox
        :param driver: browser web driver
        """
        BasePage.click_on_object(driver, locators.delete_file_button_locator)
        alert_message = "Are you sure?"
        _wait_for_alert(driver, alert_message, delay=3)
        BasePage.alert_accept_click(driver)
