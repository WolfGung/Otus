#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from mock_test.main_tests import test_check_status
from unittest.mock import patch
import unittest


class TestApi(unittest.TestCase):
    @patch('main_tests.requests.get')
    def test_status(self, mock_get):
        mock_get.return_value.status_code = 200
        responce = test_check_status()
        self.assertEqual(responce.status_code, 200)

    @patch('main_tests.requests.get')
    def test_url(self, mock_get):
        mock_get.return_value.url = "http://192.168.102.98/opencart/"
        responce = test_check_status()
        self.assertEqual(responce.url, "http://192.168.102.98/opencart/")

    @patch('main_tests.requests.get')
    def test_text_check(self, mock_get):
        mock_get.return_value.text = "test_text"
        responce = test_check_status()
        self.assertIsInstance(responce.text, str)

    @patch('main_tests.requests.get')
    def test_reason_check(self, mock_get):
        mock_get.return_value.reason = "OK"
        responce = test_check_status()
        self.assertEqual(responce.reason, "OK")

    @patch('main_tests.requests.get')
    def test_ok_check(self, mock_get):
        mock_get.return_value.ok = True
        responce = test_check_status()
        self.assertTrue(responce.ok)

    @patch('main_tests.requests.get')
    def test_apache_check(self, mock_get):
        mock_get.return_value.headers = 'Apache/2.4.29 (Ubuntu)'
        responce = test_check_status()
        self.assertIn(responce.headers, 'Apache/2.4.29 (Ubuntu)')


if __name__ == "__main__":
    unittest.main()
