#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.setup_and_teardown import *
from fives_homework.product_page import ProductPage
import logging


def test001(start_browser, address):
    """
    Test type - positive
    Add new product
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver = start_browser
    driver.get(address)
    authorize_as_admin(driver, login="support", password="elephant")
    add_new_product(driver, product_name="Test product", meta_tag="Test meta tag", model="Test model")
    filter_products_by_name(driver, product_name="Test product")
    products = ProductPage.find_product_name(driver)
    for product in products:
        logging.debug(product)
        assert "Test product" in product.text
    delete_all_products(driver)
    ProductPage.accept_product_delete(driver)


def test002(start_browser, address):
    """
    Test type - positive
    Delete product
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver = start_browser
    driver.get(address)
    authorize_as_admin(driver, login="support", password="elephant")
    add_new_product(driver, product_name="Test product", meta_tag="Test meta tag", model="Test model")
    filter_products_by_name(driver, product_name="Test product")
    delete_all_products(driver)
    ProductPage.accept_product_delete(driver)
    filter_products_by_name(driver, product_name="Test product")
    products = ProductPage.find_product_name(driver)
    for product in products:
        logging.debug(product)
        assert "Test product" not in product.text


def test003(start_browser, address):
    """
    Test type - positive
    Edit product
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver = start_browser
    driver.get(address)
    authorize_as_admin(driver, login="support", password="elephant")
    add_new_product(driver, product_name="Test product", meta_tag="Test meta tag", model="Test model")
    filter_products_by_name(driver, product_name="Test product")
    ProductPage.find_and_click_edit_button(driver)
    ProductPage.clear_product_name_field(driver)
    ProductPage.input_product_name(driver, product_name="Edited test product")
    ProductPage.save_new_product_button_click(driver)
    ProductPage.clear_filter_name_filed(driver)
    filter_products_by_name(driver, product_name="Edited test product")
    products = ProductPage.find_product_name(driver)
    for product in products:
        logging.debug(product)
        assert "Edited test product" in product.text
    filter_products_by_name(driver, product_name="Edited test product")
    delete_all_products(driver)
    ProductPage.accept_product_delete(driver)


def test004(start_browser, address):
    """
    Test type - positive
    Create new product with 3 images
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver = start_browser
    driver.get(address)
    images_names = ("image1.jpg", "image2.jpg", "image3.jpg")
    authorize_as_admin(driver, login="support", password="elephant")
    add_new_product_with_images(driver, product_name="Test product", meta_tag="Test meta tag",
                                model="Test model", images_path="/home/zhukov/Documents/nokia_images/",
                                file_names=images_names)
    delete_images_from_opencart(driver, file_names=images_names)
    MainPage.open_product_catalog(driver)
    MainPage.click_product_button(driver)
    filter_products_by_name(driver, product_name="Test product")
    delete_all_products(driver)
