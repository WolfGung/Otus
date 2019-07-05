#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from abc import ABCMeta
from html.parser import HTMLParser
from collections import Counter


class MyHTMLParser(HTMLParser, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.tag_dict = dict()
        self.tag_list = list()
        self.attr_list = list()
        self.final_dict = dict()
        self.most_frequent_tag = str()
        self.text_list = list()
        self.href_list = list()

    def handle_starttag(self, tag, attrs):
        if len(attrs) > 0:
            self.tag_dict[tag] = attrs
        self.tag_list.append(tag)
        if len(attrs) > 0:
            for i in attrs:
                self.attr_list.append(i)

    def tag_parser(self):
        count_dict = Counter(self.tag_list)
        counter = 0
        for key, value in count_dict.items():
            if counter < value:
                counter = value
                self.most_frequent_tag = key
            else:
                continue

    def text_parser(self):
        for i in self.attr_list:
            if self.attr_list[i][0] == "text":
                self.text_list.append(self.attr_list[i][1:])

    def href_parser(self):
        for i in self.attr_list:
            if self.attr_list[i][0] == "href":
                self.href_list.append(self.attr_list[i][1:])

    def final_dict_creator(self):
        self.final_dict['tags'] = self.tag_list
        self.final_dict['text'] = self.text_list
        self.final_dict['most_frequent_tag'] = self.most_frequent_tag
        self.final_dict['images and urls'] = self.href_list

    def print_all(self):
        html = MyHTMLParser()
        html.tag_parser()
        html.text_parser()
        html.href_parser()
        html.final_dict_creator()
        print(self.final_dict)
