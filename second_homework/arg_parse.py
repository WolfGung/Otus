import argparse
import logging
from .url_lists.conftest import url_list_suite_1 as url_list_1
from .url_lists.conftest import url_list_suite_2 as url_list_2
from .url_lists.conftest import url_list_suite_3 as url_list_3
from .test_suites.test_suite_1 import TestSuite1


def suite_runner():
    for value in ["1", "2", "3"]:
        print('Please enter {} to run suite {}, or "any" to run all suites'.format(value, value))
        test_url = input(str())
    suites_url_list = [url_list_1, url_list_2, url_list_3]
    parser = argparse.ArgumentParser(description="Test suite run")
    parser.add_argument("test_url", type=str, help="enter test number 1, 2, 3 or any to run all suites")
    args = parser.parse_args(test_url)
    if args.test_url == '1':
        logging.info("Running first suite")
        TestSuite1.test_header_run(url_list_1)
        TestSuite1.test_status_code_run(url_list_1)
        TestSuite1.test_status_run(url_list_1)
    if args.test_url == '2':
        logging.info("Running second suite")
        TestSuite1.test_header_run(url_list_2)
        TestSuite1.test_status_code_run(url_list_2)
        TestSuite1.test_status_run(url_list_2)
    if args.test_url == '3':
        logging.info("Running_third_suite")
        TestSuite1.test_header_run(url_list_3)
        TestSuite1.test_status_code_run(url_list_3)
        TestSuite1.test_status_run(url_list_3)
    if args.test_url == 'any':
        logging.info("Running all suites")
        for url in suites_url_list:
            TestSuite1.test_header_run(url)
            TestSuite1.test_status_code_run(url)
            TestSuite1.test_status_run(url)
