#!/usr/bin/python
# -*- coding: UTF-8 -*-


import logging
from fives_homework.locators import Locators as locators
from selenium.webdriver.common.keys import Keys


def login_input(driver, login):
    """
    Input email address to login field
    :param driver: browser web driver
    :param login: user email address
    """
    locator = locators.login_input_locator
    logging.debug("Try to find login input field with locator {}".format(*locator))
    driver.find_element(*locator).send_keys(login)


def password_input(driver, password):
    """
    Input password to password field
    :param driver: browser web driver
    :param password: user password
    """
    locator = locators.password_input_locator
    logging.debug("Try to find password input field with locator {}".format(*locator))
    driver.find_element(*locator).send_keys(password)


def accept_button_click(driver):
    """
    Click on accept button
    :param driver: browser web driver
    """
    locator = locators.login_button_locator
    logging.debug("Try to click on accept button with locator {}".format(*locator))
    driver.find_element(*locator).click()


def message_close_button_click(driver):
    """
    Click on close button of the message
    :param driver: browser web driver
    """
    locator = locators.message_close_button_locator
    driver.find_element(*locator).click()


def open_product_catalog(driver):
    """
    Open product catalog combobox
    :param driver: browser web driver
    """
    locator = locators.product_catalog_locator
    driver.find_element(*locator).click()


def click_product_button(driver):
    """
    Click on product button in the catalog
    :param driver: browser web driver
    """
    locator = locators.product_button_locator
    driver.find_element(*locator).click()


def add_new_product_button_click(driver):
    """
    Click on add new product button
    :param driver: browser web driver
    """
    locator = locators.add_new_product_locator
    driver.find_element(*locator).click()


def input_product_name(driver, product_name):
    """
    Input product name in add new product menu
    :param driver: browser web driver
    :param product_name: name of the product that we want to add
    """
    locator = locators.name_input_field_locator
    driver.find_element(*locator).send_keys(product_name)


def input_meta_tag(driver, meta_tag):
    """
    Input meta tag for new product
    :param driver: browser web driver
    :param meta_tag: meta tag of product that we want to add
    """
    locator = locators.meta_title_locator
    driver.find_element(*locator).send_keys(meta_tag)


def data_tab_click(driver):
    """
    Click on data tag for new product
    :param driver: browser web driver
    """
    locator = locators.data_tab_locator
    driver.find_element(*locator).click()


def input_model(driver, model):
    """
    Input model to the model field for product that we want to add
    :param driver: browser web driver
    :param model: model of the new product
    """
    locator = locators.model_input_field_locator
    driver.find_element(*locator).send_keys(model)


def save_new_product_button_click(driver):
    """
    Click on save new product button
    :param driver: browser web driver
    """
    locator = locators.save_new_product_button_locator
    driver.find_element(*locator).click()


def find_product_name(driver):
    """
    Find product name from the product list
    :param driver: browser web driver
    :return product
    """
    locator = locators.product_form_locator
    products = driver.find_elements(*locator)
    return products


def input_product_name_to_filter(driver, product_name):
    """
    Enter product name to the product filter
    :param driver: browser web driver
    :param product_name: product name by that we will filter products
    """
    locator = locators.product_name_filter_locator
    driver.find_element(*locator).send_keys(product_name)


def click_filter_button(driver):
    """
    Click on filter assert button
    :param driver: browser webdriver
    """
    locator = locators.filter_button_locator
    driver.find_element(*locator).click()


def click_choose_all_products_checkbox(driver):
    """
    Iter all checkboxes and found checkbox for choose all products
    :param driver: browser webdriver
    """
    locator = locators.checkboxes_locator
    buttons = driver.find_elements(*locator)
    for button in buttons:
        onclick_text = button.get_attribute('onclick')
        if onclick_text == "$('input[name*=\'selected\']').prop('checked', this.checked);":
            button.click()
            break
        else:
            logging.error("There are no button with onclick text =" 
                          "$('input[name*=\'selected\']').prop('checked', this.checked);")


def click_delete_all_products_button(driver):
    """
    Delete all choosed products
    :param driver: browser webdriver
    """
    locator = locators.delete_products_locator
    driver.find_element(*locator).click()
    driver.find_element(*locator).send_keys(Keys.ENTER)


def find_and_click_edit_button(driver):
    """
    Find from buttons edit button and click it
    :param driver: browser webdriver
    """
    locator = locators.edit_product_button_locator
    buttons = driver.find_elements(*locator)
    for button in buttons:
        data_title = button.get_attribute('data-original-title')
        if data_title == "Edit":
            button.click()
            break
        else:
            logging.error("There are no button with data_title = 'Edit'")


def clear_product_name_field(driver):
    """
    Clear the product name field
    :param driver: browser webdriver
    """
    locator = locators.name_input_field_locator
    driver.find_element(*locator).clear()