#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


import requests
import unittest


class Tester(unittest.TestCase):
    @staticmethod
    def test_check_status():
        status = requests.get("http://192.168.102.98/opencart/").status_code
        assert status == 200, 'incorrect opencart status'

    @staticmethod
    def test_check_url():
        url = requests.get("http://192.168.102.98/opencart/").url
        assert url == "http://192.168.102.98/opencart/", 'wrong url'

    @staticmethod
    def test_text_check():
        text = requests.get("http://192.168.102.98/opencart/").text
        assert isinstance(text, str), 'there are no text'

    @staticmethod
    def test_reason_check():
        reason = requests.get("http://192.168.102.98/opencart/").reason
        assert reason == 'OK', 'something wrong with reason'

    @staticmethod
    def test_ok_check():
        ok = requests.get("http://192.168.102.98/opencart/").ok
        assert ok is True, 'opencart not ok'

    @staticmethod
    def test_apache_check():
        ap = requests.get("http://192.168.102.98/opencart/").headers
        assert ap['Server'] == 'Apache/2.4.29 (Ubuntu)', 'Server is {}'.format(ap['Server'])

