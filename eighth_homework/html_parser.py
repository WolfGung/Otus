#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from abc import ABCMeta
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser, metaclass=ABCMeta):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)
