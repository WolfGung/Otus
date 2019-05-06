#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.product_page import ProductPage
from fives_homework.main_page import MainPage
from fives_homework.admin_login_page import AdminLoginPage
import logging


def authorize_as_admin(driver, login, password):
    AdminLoginPage.login_input(driver=driver, login=login)
    AdminLoginPage.password_input(*driver, password)
    AdminLoginPage.accept_button_click(*driver)
    logging.info("Authorization has been successful")
    MainPage.message_close_button_click(*driver)


def add_new_product(driver, product_name, meta_tag, model):
    MainPage.open_product_catalog(*driver)
    MainPage.click_product_button(*driver)
    ProductPage.add_new_product_button_click(*driver)
    ProductPage.input_product_name(*driver, product_name)
    ProductPage.input_meta_tag(*driver, meta_tag)
    ProductPage.data_tab_click(*driver)
    ProductPage.input_model(*driver, model)
    ProductPage.save_new_product_button_click(*driver)
    logging.info("Product has been created")


def filter_products_by_name(driver, product_name):
    ProductPage.input_product_name_to_filter(*driver, product_name)
    ProductPage.click_filter_button(driver)
    logging.info("Products has been filtered by name:{}".format(product_name))


def delete_all_products(driver):
    ProductPage.click_choose_all_products_checkbox(driver)
    ProductPage.click_delete_all_products_button(driver)
    logging.info("All products has been deleted")
