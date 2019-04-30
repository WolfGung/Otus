#!/usr/bin/python
# -*- coding: UTF-8 -*-


from selenium.webdriver.common.by import By


class Locators:
    email_input_locator = (By.ID, "input-email")
    password_input_locator = (By.ID, "input-password")
    login_button_locator = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/input")
    warning_locator = (By.XPATH, "/html/body/div[2]/div[1]")
