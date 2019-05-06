#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.locators import Locators as locators
from fives_homework.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self):
        self.add_product_locator = locators.add_new_product_locator
        self.new_product_name_field_locator = locators.name_input_field_locator
        self.new_product_meta_field_locator = locators.meta_title_locator
        self.new_product_data_locator = locators.data_tab_locator
        self.new_product_model_field_locator = locators.model_input_field_locator
        self.new_product_save_button_locator = locators.save_new_product_button_locator
        self.product_form_locator = locators.product_form_locator
        self.product_filter_name_field_locator = locators.product_name_filter_locator
        self.product_filter_accept_button_locator = locators.filter_button_locator
        self.checkboxes_locators = locators.checkboxes_locator
        self.delete_products_button_locator = locators.delete_products_locator
        self.edit_button_locator = locators.edit_product_button_locator

    def add_new_product_button_click(self, driver):
        """
        Click on add new product button
        :param driver: browser web driver
        """
        self.click_on_object(driver, locator=self.add_product_locator)

    def input_product_name(self, driver, product_name):
        """
        Input product name in add new product menu
        :param driver: browser web driver
        :param product_name: name of the product that we want to add
        """
        self.send_keys_to_object(driver, locator=self.new_product_name_field_locator, some_keys=product_name)

    def input_meta_tag(self, driver, meta_tag):
        """
        Input meta tag for new product
        :param driver: browser web driver
        :param meta_tag: meta tag of product that we want to add
        """
        self.send_keys_to_object(driver, locator=self.new_product_meta_field_locator, some_keys=meta_tag)

    def data_tab_click(self, driver):
        """
        Click on data tag for new product
        :param driver: browser web driver
        """
        self.click_on_object(driver, locator=self.new_product_data_locator)

    def input_model(self, driver, model):
        """
        Input model to the model field for product that we want to add
        :param driver: browser web driver
        :param model: model of the new product
        """
        self.send_keys_to_object(driver, locator=self.new_product_model_field_locator, some_keys=model)

    def save_new_product_button_click(self, driver):
        """
        Click on save new product button
        :param driver: browser web driver
        """
        self.click_on_object(driver, locator=self.new_product_save_button_locator)

    def find_product_name(self, driver):
        """
        Find product name from the product list
        :param driver: browser web driver
        :return product
        """
        products = driver.find_elements(self.product_form_locator)
        return products

    def input_product_name_to_filter(self, driver, product_name):
        """
        Enter product name to the product filter
        :param driver: browser web driver
        :param product_name: product name by that we will filter products
        """
        self.send_keys_to_object(driver, locator=self.product_filter_name_field_locator, some_keys=product_name)

    def click_filter_button(self, driver):
        """
        Click on filter assert button
        :param driver: browser web driver
        """
        self.click_on_object(driver, locator=self.product_filter_accept_button_locator)

    def click_choose_all_products_checkbox(self, driver):
        """
        Iter all checkboxes and found checkbox for choose all products
        :param driver: browser web driver
        """
        self.click_on_object_from_many(driver, locator=self.checkboxes_locators,
                                       attribute='type', attribute_value='checkbox')

    def click_delete_all_products_button(self, driver):
        """
        Delete all choosed products
        :param driver: browser web driver
        """
        self.click_on_object(driver, locator=self.delete_products_button_locator)

    def find_and_click_edit_button(self, driver):
        """
        Find from buttons edit button and click it
        :param driver: browser webd river
        """
        self.click_on_object_from_many(driver, locator=self.edit_button_locator,
                                       attribute='data-original-title', attribute_value='Edit')

    def clear_product_name_field(self, driver):
        """
        Clear the product name field
        :param driver: browser web driver
        """
        self.clear_object(driver, locator=self.new_product_name_field_locator)

    def accept_product_delete(self, driver):
        """
        Accept project delete message
        :param driver: browser web driver
        """
        self.alert_accept_click(driver)
