#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from robot.api.deco import keyword
from selenium import webdriver


class AdminOpencart:
    @keyword(name="Admin opencart test")
    def admin_opencart_login(self):
        driver = webdriver.Firefox()
        driver.get('http://192.168.102.98/opencart/admin/')
        el = driver.find_element_by_id("input-username")
        el.send_keys("support")
        el = driver.find_element_by_id("input-password")
        el.send_keys("elephant")
        el = driver.find_element_by_xpath("//button[@type='submit']")
        el.click()
        try:
            el = driver.find_element_by_xpath("//button[@class='close']")
            el.click()
        except Exception:
            print("There are no alert! May be u didn't login?")
        finally:
            driver.close()
