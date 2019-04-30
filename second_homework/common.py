import requests
import logging


class TestCases:
    @staticmethod
    def status_response_check(request):
        r = requests.get(str(request))
        r_status = r.status_code
        logging.debug("Response status code:{}".format(r_status))
        assert r_status == 200

    @staticmethod
    def status_json_response_check(request):
        r = requests.get(str(request)).json()
        r_status = r.get("status")
        logging.debug("Response status:{}".format(r_status))
        assert r_status == "success"

    @staticmethod
    def headers_response_check(request):
        r = requests.get(str(request))
        r_headers = r.headers
        logging.debug("Response headers:{}".format(r_headers))
        assert len(r_headers) > 0
