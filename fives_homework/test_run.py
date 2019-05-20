#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.setup_and_teardown import *
from fives_homework.menu_constructor import MenuConstructor
from fives_homework.opencart_logger import web_logging, proxy_logging
from fives_homework.product_page import ProductPage


def test001(start_browser, address):
    """
    Test type - positive
    Add new product
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver, proxy = start_browser
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
    proxy_logging(proxy)
    web_logging(driver, log_file='web_log.log')


def test002(start_browser, address):
    """
    Test type - positive
    Delete product
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver, proxy = start_browser
    driver.get(address)
    authorize_as_admin(driver, login="support", password="elephant")
    add_new_product(driver, product_name="Test product", meta_tag="Test meta tag", model="Test model")
    filter_products_by_name(driver, product_name="Test product")
    delete_all_products(driver)
    ProductPage.accept_product_delete(driver)
    filter_products_by_name(driver, product_name="Test product")
    products = ProductPage.find_product_name(driver)
    for product in products:
        assert "Test product" not in product.text
    proxy_logging(proxy)
    web_logging(driver, log_file='web_log.log')


def test003(start_browser, address):
    """
    Test type - positive
    Edit product
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver, proxy = start_browser
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
        assert "Edited test product" in product.text
    filter_products_by_name(driver, product_name="Edited test product")
    delete_all_products(driver)
    ProductPage.accept_product_delete(driver)
    proxy_logging(proxy)
    web_logging(driver, log_file='web_log.log')


def test004(start_browser, address):
    """
    Test type - positive
    Create new product with 3 images
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver, proxy = start_browser
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
    proxy_logging(proxy)
    web_logging(driver, log_file='web_log.log')


def test005(start_browser, address):
    """
    Test type - positive
    Add new file to downloads menu
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver, proxy = start_browser
    driver.get(address)
    file_url = "/home/zhukov/Pictures/opencart_images/index.jpeg"
    authorize_as_admin(driver, login="support", password="elephant")
    add_file_to_opencart(driver, file_url, file_name="Test file")
    DownloadsPage.select_downloaded_file(driver)
    DownloadsPage.delete_selected_file(driver)
    proxy_logging(proxy)
    web_logging(driver, log_file='web_log.log')

def test006(start_browser, address):
    """
    Test type - positive
    add new menu field and drug and drop it
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver, proxy = start_browser
    driver.get(address)
    demo_authorize_as_admin(driver, login="demo", password="demo")
    add_new_menu_field(driver)
    MenuConstructor.check_computer_element(driver)
