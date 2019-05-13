#!/usr/bin/python
# -*- coding: UTF-8 -*-


from selenium.webdriver.common.by import By


class Locators:
    login_input_locator = (By.ID, "input-username")
    password_input_locator = (By.ID, "input-password")
    login_button_locator = (By.CLASS_NAME, "btn.btn-primary")
    message_close_button_locator = (By.CLASS_NAME, "close")
    product_catalog_locator = (By.ID, "menu-catalog")
    product_button_locator = (By.LINK_TEXT, "Products")
    add_new_product_locator = (By.CLASS_NAME, "btn.btn-primary")
    name_input_field_locator = (By.ID, "input-name1")
    meta_title_locator = (By.ID, "input-meta-title1")
    data_tab_locator = (By.XPATH, "//a[@href='#tab-data']")
    model_input_field_locator = (By.ID, "input-model")
    save_new_product_button_locator = (By.CLASS_NAME, "btn.btn-primary")
    product_form_locator = (By.CLASS_NAME, "table.table-bordered.table-hover")
    product_name_filter_locator = (By.ID, "input-name")
    filter_button_locator = (By.ID, "button-filter")
    checkboxes_locator = (By.CSS_SELECTOR, "input")
    delete_products_locator = (By.CLASS_NAME, "btn.btn-danger")
    edit_product_button_locator = (By.CLASS_NAME, "btn.btn-primary")
    image_download_button_locator = (By.ID, "button-upload")
    image_download_dynamic_locator = (By.XPATH, "//input[@name='file[]']")
    image_tab_button_locator = (By.XPATH, "//a[@href='#tab-image']")
    product_image_locator = (By.ID, "thumb-image")
    image_edit_button_locator = (By.ID, "button-image")
    image_download_close_button_locator = (By.CLASS_NAME, "close")
    add_image_locator = (By.CLASS_NAME, "btn.btn-primary")
    delete_images_button_locator = (By.ID, "button-delete")
    downloads_menu_products_locator = (By.LINK_TEXT, "Downloads")
    add_new_downloads_file_locator = (By.XPATH, '//a[@data-original-title="Add New"]')
    download_name_field_locator = (By.CLASS_NAME, "form-control")
    file_upload_button_locator = (By.ID, "button-upload")
    file_download_dynamic_locator = (By.XPATH, "//input[@name='file']")
    save_downloaded_file = (By.CLASS_NAME, "btn.btn-primary")
    check_box_type_locator = (By.XPATH, "//input[@type='checkbox']")
    delete_file_button_locator = (By.XPATH, "//button[@data-original-title='Delete']")
