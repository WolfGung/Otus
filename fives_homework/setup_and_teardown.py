#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fives_homework.product_page import ProductPage
from fives_homework.main_page import MainPage
from fives_homework.admin_login_page import AdminLoginPage
import logging


def authorize_as_admin(driver, login, password):
    AdminLoginPage.login_input(driver, login)
    AdminLoginPage.password_input(driver, password)
    AdminLoginPage.accept_button_click(driver)
    logging.info("Authorization has been successful")
    MainPage.message_close_button_click(driver)


def add_new_product(driver, product_name, meta_tag, model):
    MainPage.open_product_catalog(driver)
    MainPage.click_product_button(driver)
    ProductPage.add_new_product_button_click(driver)
    ProductPage.input_product_name(driver, product_name)
    ProductPage.input_meta_tag(driver, meta_tag)
    ProductPage.data_tab_click(driver)
    ProductPage.input_model(driver, model)
    ProductPage.save_new_product_button_click(driver)
    logging.info("Product has been created")


def filter_products_by_name(driver, product_name):
    ProductPage.input_product_name_to_filter(driver, product_name)
    ProductPage.click_filter_button(driver)
    logging.info("Products has been filtered by name:{}".format(product_name))


def delete_all_products(driver):
    ProductPage.click_choose_all_products_checkbox(driver)
    ProductPage.click_delete_all_products_button(driver)
    logging.info("All products has been deleted")


def add_new_product_with_images(driver, product_name, meta_tag, model, images_path, file_names):
    MainPage.open_product_catalog(driver)
    MainPage.click_product_button(driver)
    ProductPage.add_new_product_button_click(driver)
    ProductPage.input_product_name(driver, product_name)
    ProductPage.input_meta_tag(driver, meta_tag)
    ProductPage.data_tab_click(driver)
    ProductPage.input_model(driver, model)
    ProductPage.click_on_image_tab(driver)
    ProductPage.click_on_image(driver)
    ProductPage.click_on_edit_image_button(driver)
    ProductPage.add_new_images_to_store(driver, images_path, *file_names)
    ProductPage.close_add_image_menu()
    ProductPage.add_images_to_product(driver, *file_names)
#    ProductPage.print_image_link(driver)
    logging.info("Product has been created")


def delete_images_from_opencart(driver, file_names):
    MainPage.open_product_catalog(driver)
    MainPage.click_product_button(driver)
    ProductPage.add_new_product_button_click(driver)
    ProductPage.click_on_image_tab(driver)
    ProductPage.click_on_image(driver)
    ProductPage.click_on_edit_image_button(driver)
    ProductPage.choose_remove_images_by_names(driver, file_names)
    ProductPage.delete_selected_images(driver)
    ProductPage.close_add_image_menu()
