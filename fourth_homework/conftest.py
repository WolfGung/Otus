#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.chrome.options import Options as chrome_options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox",
                     help="Enter browser name. Supported:'firefox', 'chrome'")


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
    chromedriver_path = '/home/zhukov/Otus/Otus_project/drivers/chromedriver'
    firefoxdriver_path = '/home/zhukov/Otus/Otus_project/drivers/geckodriver'
    if browser == "chrome":
        options = chrome_options()
        options.headless = True
        wd = webdriver.Chrome(options=options, executable_path=chromedriver_path)
    else:
        options = firefox_options()
        options.headless = True
        wd = webdriver.Firefox(options=options, executable_path=firefoxdriver_path)
    wd.get("http://192.168.102.98/opencart/index.php?route=account/login")
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd
