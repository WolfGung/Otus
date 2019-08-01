#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


import requests


def test_check_status():
    response = requests.get("http://192.168.102.98/opencart/")
    if response.ok:
        return response
    else:
        return None
