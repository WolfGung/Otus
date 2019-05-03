#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.setup_and_teardown import *


def test001(start_browser, address, timeout):
    """
    Test type - positive
    Add new product
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    :param timeout: page load timeout
    """
    driver = start_browser
    driver.get(address, timeout)
    authorize_as_admin(driver, login="support", password="elephant")
    add_new_product(driver, product_name="Test product", meta_tag="Test meta tag", model="Test model")
    filter_products_by_name(driver, product_name="Test product")
    products = find_product_name(driver)
    for product in products:
        logging.debug(product)
        assert "Test product" in product.text
    delete_all_products(driver)
    alert_accept_click(driver)


def test002(start_browser, address, timeout):
    """
    Test type - positive
    Delete product
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    :param timeout: page load timeout
    """
    driver = start_browser
    driver.get(address, timeout)
    authorize_as_admin(driver, login="support", password="elephant")
    add_new_product(driver, product_name="Test product", meta_tag="Test meta tag", model="Test model")
    filter_products_by_name(driver, product_name="Test product")
    delete_all_products(driver)
    alert_accept_click(driver)
    products = find_product_name(driver)
    for product in products:
        logging.debug(product)
        assert "Test product" not in product.text


def test003(start_browser, address, timeout):
    """
    Test type - positive
    Edit product
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    :param timeout: page load timeout
    """
    driver = start_browser
    driver.get(address, timeout)
    authorize_as_admin(driver, login="support", password="elephant")
    add_new_product(driver, product_name="Test product", meta_tag="Test meta tag", model="Test model")
    filter_products_by_name(driver, product_name="Test product")
    find_and_click_edit_button(driver)
    clear_product_name_field(driver)
    input_product_name(driver, product_name="Edited test product")
    filter_products_by_name(driver, product_name="Edited test product")
    products = find_product_name(driver)
    for product in products:
        logging.debug(product)
        assert "Edited test product" in product.text
    delete_all_products(driver)
    alert_accept_click(driver)

