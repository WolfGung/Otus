#!/usr/bin/python
# -*- coding: UTF-8 -*-


from selenium.webdriver.support.events import AbstractEventListener
import logging


class OpencartListener(AbstractEventListener):
    logging.basicConfig(filename='test_run_log.log', level=logging.disable(10))

    def before_find(self, by, value, driver):
        logging.info("trying to find by{}:{}".format(by, value))

    def after_find(self, by, value, driver):
        logging.info(by, value, "element found!")

    def before_click(self, element, driver):
        logging.info("trying to click on {}".format(element))

    def after_click(self, element, driver):
        logging.info("click on {} has been success!".format(element))

    def on_exception(self, exception, driver):
        driver.save_screenshot("./exception_screenshot.png")
        logging.error(exception)

    def before_quit(self, driver):
        logging.info("Starting browser")

    def after_quit(self, driver):
        logging.info("Quiting browser")


def web_logging(driver, log_file="web_log.log"):
    """
    Browser logging function
    :param driver: browser web driver
    :param log_file: path to the log file
    """
    web_logs = open(log_file, 'w')
    for string in driver.get_log("performance"):
        web_logs.write(string + '\n')
    web_logs.close()


def proxy_logging(proxy, log_file="proxy_logs.log"):
    """
    Proxy logging function
    :param proxy: browsermob proxy
    :param log_file: path to the log file
    """
    proxy_logs = open(log_file, 'w')
    proxy_logs.write(str(proxy.har))
    proxy_logs.close()
