#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


import socket
from eighth_homework.html_parser import MyHTMLParser
from eighth_homework.parametrization import Parametrization


class Socket:
    def __init__(self):
        self.parametrization = Parametrization()
        self.host = self.parametrization.host_parser()
        self.port = self.parametrization.port_parser()
        self.method = self.parametrization.method_parser()
        self.headline, self.headline_data = self.parametrization.headline_parser()

    def socket_connect(self):
        request = "{} / HTTP/1.1\n{}: {}\n\n".format(self.method,
                                                     self.headline,
                                                     self.headline_data)
        address = (self.host, self.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(address)
        sock.send(request.encode())
        result = sock.recv(4096)
        data = (result.decode(encoding="ISO-8859-1"))
        sock.close()
        return data

    def dict_data_parser(self):
        some_data = (self.socket_connect().split('\n'))
        final_dict = dict()
        for i in some_data:
            new_str = i.split()
            if len(new_str) > 1:
                final_dict[new_str[0]] = new_str[1:]
            else:
                continue
        for keys, values in final_dict.items():
            print(keys, values)

    def html_data_parser(self):
        parser = MyHTMLParser()
        parser.feed(self.socket_connect())
        parser.print_all()
