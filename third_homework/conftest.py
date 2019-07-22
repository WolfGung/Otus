#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.chrome.options import Options as chrome_options


def pytest_addoption(parser):
    """
    the command line parameters module
    """
    parser.addoption("--browser", action="store", default="firefox",
                     help="Enter browser name. Supported:'firefox', 'chrome'")
    parser.addoption("--address", action="store", default="http://192.168.0.103/",
                     help="Enter opencart url")


@pytest.fixture
def browser(request):
    parameter = request.config.getoption("--browser")
    return parameter


@pytest.fixture
def start_browser(request, browser):
    """
    Setup and run browser
    :param request: pytest request
    :param browser: name of browser that will start
    """
    chromedriver_path = '/home/support/Py_projects/Otus/drivers/chromedriver'
    firefoxdriver_path = '/home/support/Py_projects/Otus/drivers/geckodriver'
    if browser == "chrome":
        options = chrome_options()
        options.headless = True
        wd = webdriver.Chrome(options=options, executable_path=chromedriver_path)
    else:
        options = firefox_options()
        options.headless = True
        wd = webdriver.Firefox(options=options, executable_path=firefoxdriver_path)
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def open_login_page(request, start_browser):
    """
    Opencart start page
    """
    url = 'opencart/index.php?route=account/login'
    parametrized_url = request.config.getoption("--address")
    opencart_address = str(parametrized_url)+str(url)
    return opencart_address

