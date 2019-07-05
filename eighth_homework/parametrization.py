#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


class Parametrization:
    def __init__(self):
        self.method = None
        self.headline = None
        self.host = None
        self.port = None
        self.headline_data = None

    def method_parser(self):
        self.method = input("Please enter method...")
        if self.method == '':
            self.method = "GET"
        return self.method

    def headline_parser(self):
        self.headline = input("Please enter headline...")
        if self.headline != '':
            self.headline_data = input("Please enter headline data...")
        if self.headline == '':
            self.headline = "Host"
            self.headline_data = "localhost"
        return self.headline, self.headline_data

    def host_parser(self):
        self.host = input("Please enter host...")
        if self.host == '':
            self.host = "google.com"
        return self.host

    def port_parser(self):
        self.port = input("Please enter port...")
        if self.port == '':
            self.port = 80
        return self.port
