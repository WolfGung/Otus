#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pytest
from selenium import webdriver
from fives_homework.opencart_logger import OpencartListener
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from browsermobproxy import Server
import urllib.parse


server = Server(r"/home/zhukov/Tools/browsermob-proxy-2.1.4/bin/browsermob-proxy")
server.start()

proxy = server.create_proxy()
proxy.new_har()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox",
                     help="Enter browser name. Supported:'firefox', 'chrome'")
    parser.addoption("--address", action="store",
                     default="http://192.168.102.98/opencart/admin/",
                     help="Enter opencart url")
    parser.addoption("--timeout", action="store", default="5",
                     help="Enter page load timeout")


@pytest.fixture
def timeout(request):
    """
    Getting page load timeout
    """
    parameter = request.config.getoption("--timeout")
    return parameter


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
def start_browser(request, browser, timeout):
    """
    Setup and run browser
    :param request: pytest request
    :param browser: name of browser that will start
    :param timeout: page load timeout
    :return wd: web driver
    :return proxy: browsermob proxy
    """
    chromedriver_path = '/home/zhukov/PycharmProjects/Otus/drivers/chromedriver'
    firefoxdriver_path = '/home/zhukov/PycharmProjects/Otus/drivers/geckodriver'
    url = urllib.parse.urlparse(proxy.proxy).path
    if browser == "chrome":
        des_cap = DesiredCapabilities.CHROME
        des_cap['loggingPrefs'] = {'performance': 'ALL'}
        chrome_options().add_argument(argument='--proxy-server={}'.format(url))
        options = chrome_options()
        options.headless = True
        wd = EventFiringWebDriver(webdriver.Chrome(options=options, executable_path=chromedriver_path,
                                                   desired_capabilities=des_cap), OpencartListener())
        wd.implicitly_wait(int(timeout))
    else:
        des_cap = DesiredCapabilities.FIREFOX
        des_cap['loggingPrefs'] = {'performance': 'ALL'}
        firefox_options().add_argument(argument='--proxy-server={}'.format(url))
        options = firefox_options()
#        options.headless = True
        wd = EventFiringWebDriver(webdriver.Firefox(options=options, executable_path=firefoxdriver_path,
                                                    desired_capabilities=des_cap), OpencartListener())
        wd.implicitly_wait(int(timeout))
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd, proxy
