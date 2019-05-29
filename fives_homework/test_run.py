#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


import pytest
from fives_homework.setup_and_teardown import *
from fives_homework.menu_constructor import MenuConstructor
from fives_homework.opencart_logger import web_logging, proxy_logging
from fives_homework.product_page import ProductPage
import allure


@allure.title('001 Critical: Creating new product')
@allure.severity("critical")
@pytest.mark.env("opencart")
def test001(start_browser, address):
    """
    Test type - positive
    Add new product
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver, proxy = start_browser
    driver.get(address)
    with allure.step('Authorization in admin login mask'):
        authorize_as_admin(driver, login="support", password="elephant")
    with allure.step('Adding new product'):
        add_new_product(driver, product_name="Test product", meta_tag="Test meta tag", model="Test model")
        filter_products_by_name(driver, product_name="Test product")
    with allure.step('Looking for created product'):
        products = ProductPage.find_product_name(driver)
        for product in products:
            logging.debug(product)
            assert "Test product" in product.text
    with allure.step('Removing product'):
        delete_all_products(driver)
        ProductPage.accept_product_delete(driver)
#    proxy_logging(proxy)
#    web_logging(driver, log_file='web_log.log')


@allure.title('002 Critical: Remove new product')
@allure.severity("critical")
@pytest.mark.env("opencart")
def test002(start_browser, address):
    """
    Test type - positive
    Delete product
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver, proxy = start_browser
    driver.get(address)
    with allure.step('Authorization in admin login mask'):
        authorize_as_admin(driver, login="support", password="elephant")
    with allure.step('Adding new product'):
        add_new_product(driver, product_name="Test product", meta_tag="Test meta tag", model="Test model")
    with allure.step('Removing product'):
        filter_products_by_name(driver, product_name="Test product")
        delete_all_products(driver)
        ProductPage.accept_product_delete(driver)
    with allure.step('Looking for removed product'):
        filter_products_by_name(driver, product_name="Test product")
        products = ProductPage.find_product_name(driver)
        for product in products:
            assert "Test product" not in product.text
#     proxy_logging(proxy)
#     web_logging(driver, log_file='web_log.log')


@allure.title('003 Critical: Edit product')
@allure.severity("critical")
@pytest.mark.env("opencart")
def test003(start_browser, address):
    """
    Test type - positive
    Edit product
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver, proxy = start_browser
    driver.get(address)
    with allure.step('Authorization in admin login mask'):
        authorize_as_admin(driver, login="support", password="elephant")
    with allure.step('Adding new product'):
        add_new_product(driver, product_name="Test product", meta_tag="Test meta tag", model="Test model")
    with allure.step('Editing product'):
        filter_products_by_name(driver, product_name="Test product")
        ProductPage.find_and_click_edit_button(driver)
        ProductPage.clear_product_name_field(driver)
        ProductPage.input_product_name(driver, product_name="Edited test product")
        ProductPage.save_new_product_button_click(driver)
    with allure.step('Looking for edited product'):
        ProductPage.clear_filter_name_filed(driver)
        filter_products_by_name(driver, product_name="Edited test product")
        products = ProductPage.find_product_name(driver)
        for product in products:
            assert "Edited test product" in product.text
    with allure.step('Removing product'):
        filter_products_by_name(driver, product_name="Edited test product")
        delete_all_products(driver)
        ProductPage.accept_product_delete(driver)
#     proxy_logging(proxy)
#     web_logging(driver, log_file='web_log.log')


@allure.title('004 Critical: Create new product with three images')
@allure.severity("critical")
@pytest.mark.env("opencart")
def test004(start_browser, address):
    """
    Test type - positive
    Create new product with 3 images
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver, proxy = start_browser
    driver.get(address)
    images_names = ("image1", "image2", "image3")
    jpg_names = list()
    for name in images_names:
        jpg_names.append(str(name)+".jpg")
    with allure.step('Authorization in admin login mask'):
        authorize_as_admin(driver, login="support", password="elephant")
    with allure.step('Adding new product with image'):
        add_new_product_with_images(driver, product_name="Test product", meta_tag="Test meta tag",
                                model="Test model", images_path="/home/zhukov/Documents/nokia_images/",
                                file_names=jpg_names)
    with allure.step('Looking for product images by names'):
        ProductPage.check_images_names(driver, images_names)
    with allure.step('Removing images'):
        delete_images_from_opencart(driver, file_names=jpg_names)
    with allure.step('Removing product'):
        MainPage.open_product_catalog(driver)
        MainPage.click_product_button(driver)
        filter_products_by_name(driver, product_name="Test product")
        delete_all_products(driver)
# proxy_logging(proxy)
# web_logging(driver, log_file='web_log.log')


@allure.title('005 Critical: Add new file to "downloads" menu')
@allure.severity("critical")
@pytest.mark.env("opencart")
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
    with allure.step('Authorization in admin login mask'):
        authorize_as_admin(driver, login="support", password="elephant")
    with allure.step('Adding file to opencart'):
        add_file_to_opencart(driver, file_url, file_name="Test file")
    with allure.step('Removing downloaded file'):
        DownloadsPage.select_downloaded_file(driver)
        DownloadsPage.delete_selected_file(driver)
#     proxy_logging(proxy)
#     web_logging(driver, log_file='web_log.log')


@allure.title('006 Critical: drug and drop new menu field in menu constructor')
@allure.severity("critical")
@pytest.mark.env("demo")
def test006(start_browser, address):
    """
    Test type - positive
    add new menu field and drug and drop it
    :param start_browser: browser run
    :param address: fixture with parametrized url of opencart
    """
    driver, proxy = start_browser
    driver.get(address)
    with allure.step('Authorization in admin login mask'):
        demo_authorize_as_admin(driver, login="demo", password="demo")
    with allure.step('Adding new menu field'):
        add_new_menu_field(driver)
    with allure.step('Looking for added menu field'):
        MenuConstructor.check_computer_element(driver)
#    proxy_logging(proxy)
#    web_logging(driver, log_file='web_log.log')
