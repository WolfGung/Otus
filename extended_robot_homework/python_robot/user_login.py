#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from robot.api.deco import keyword
from selenium import webdriver


class UserOpencart:
    @keyword(name="User opencart test")
    def user_opencart_login(self):
        driver = webdriver.Firefox()
        driver.get('http://192.168.102.98/opencart/')
        el = driver.find_element_by_xpath("//a[@title='My Account']")
        el.click()
        el = driver.find_element_by_xpath("//a[@href='http://192.168.102.98/opencart/index.php?route=account/login']")
        el.click()
        el = driver.find_elements_by_id("input-email")
        el.send_keys("support@otus.ru")
        el = driver.find_elements_by_id("input-password")
        el.send_keys("elephant")
        el = driver.find_element_by_xpath("//input[@type='submit']")
        el.click()
        el = driver.find_element_by_xpath("//a[@title='My Account']")
        el.click()
        try:
            el = driver.find_element_by_xpath("//a[@href='http://192.168.102.98/"
                                              "opencart/index.php?route=account/logout']")
            el.click()
        except Exception:
            print("There are no logout button! May be u didn't login?")
        finally:
            driver.close()
