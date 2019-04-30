from ..common import TestCases


class TestSuite1:
    @staticmethod
    def test_status_code_run(url_list):
        for url in url_list:
            TestCases.status_response_check(url)

    @staticmethod
    def test_status_run(url_list):
        for url in url_list:
            TestCases.status_json_response_check(url)

    @staticmethod
    def test_header_run(url_list):
        for url in url_list:
            TestCases.headers_response_check(url)
