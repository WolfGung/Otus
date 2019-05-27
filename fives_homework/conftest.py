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
import platform
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

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
    parser.addoption("-E", action="store", metavar="NAME", help="only run tests matching the environment NAME")


@pytest.fixture(scope="session")
def environment_info():
    os_platform = platform.platform()
    linux_dist = platform.linux_distribution()
    return os_platform, linux_dist


@pytest.mark.usefixtures("environment_info")
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request, environment_info):
    request.config._metadata.update(
        {"browser": request.config.getoption("--browser"),
         "address": request.config.getoption("--address")})
    yield


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        report.test_metadata = 'whatever'
        report.stage_metadata = {
            'Test status': 'start of run'
        }
    elif report.when == 'setup':
        report.stage_metadata = {
            'Test status': 'in progress'
        }
    elif report.when == 'teardown':
        report.stage_metadata = {
            'Test status': 'test finished'
        }


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
    url = urlparse(proxy.proxy).path
    if browser == "chrome":
        des_cap = DesiredCapabilities.CHROME
        des_cap['loggingPrefs'] = {'performance': 'ALL'}
        chrome_options().add_argument(argument='--proxy-server={}'.format(url))
        options = chrome_options()
        options.headless = True
        wd = EventFiringWebDriver(webdriver.Chrome(options=options, executable_path=chromedriver_path,
                                                   desired_capabilities=des_cap), OpencartListener())
#         command_executor = 'http://wolfgung1:b4sFyTQzEQanvH2GJgwg@hub.browserstack.com:80/wd/hub'
#         wd = EventFiringWebDriver(webdriver.Remote(command_executor,
#                                                    desired_capabilities={"browserName": "chrome",
#                                                                          'os': 'Linux', 'os_version': '16.04'}),
#                                  OpencartListener())
        wd.implicitly_wait(int(timeout))
    else:
        des_cap = DesiredCapabilities.FIREFOX
        des_cap['loggingPrefs'] = {'performance': 'ALL'}
        firefox_options().add_argument(argument='--proxy-server={}'.format(url))
        options = firefox_options()
        options.headless = True
        wd = EventFiringWebDriver(webdriver.Firefox(options=options, executable_path=firefoxdriver_path,
                                                    desired_capabilities=des_cap), OpencartListener())
#         command_executor = 'http://wolfgung1:b4sFyTQzEQanvH2GJgwg@hub.browserstack.com:80/wd/hub'
#         wd = EventFiringWebDriver(webdriver.Remote(command_executor,
#                                                    desired_capabilities={"browserName": "firefox",
#                                                                          'os': 'Windows', 'os_version': '10'}),
#                                   OpencartListener())
        wd.implicitly_wait(int(timeout))
    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd, proxy
