#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.chrome.options import Options as chrome_options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox",
                     help="Enter browser name. Supported:'firefox', 'chrome'")
    parser.addoption("--address", action="store",
                     default="http://192.168.0.103/opencart/index.php?route=account/login",
                     help="Enter opencart url")


@pytest.fixture
def browser(request):
    """
    Getting input browser name
    """
    parameter = request.config.getoption("--browser")
    return parameter


@pytest.fixture(scope="session")
def address(request):
    """
    Getting input address
    """
    parameter = request.config.getoption("--address")
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
