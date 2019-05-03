#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.base_page import *


def authorize_as_admin(driver, login, password):
    login_input(driver, login)
    password_input(driver, password)
    accept_button_click(driver)
    logging.info("Authorization has been successful")
    message_close_button_click(driver)


def add_new_product(driver, product_name, meta_tag, model):
    open_product_catalog(driver)
    click_product_button(driver)
    add_new_product_button_click(driver)
    input_product_name(driver, product_name)
    input_meta_tag(driver, meta_tag)
    data_tab_click(driver)
    input_model(driver, model)
    save_new_product_button_click(driver)


def filter_products_by_name(driver, product_name):
    input_product_name_to_filter(driver, product_name)
    click_filter_button(driver)


def delete_all_products(driver):
    click_choose_all_products_checkbox(driver)
    click_delete_all_products_button(driver)
