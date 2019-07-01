#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


import socket
from eighth_homework.html_parser import MyHTMLParser


def socket_connect(host='www.google.com',
                   port=80,
                   family=socket.AF_INET,
                   sock_type=socket.SOCK_STREAM,
                   request="GET / HTTP/1.1\nHost: localhost\n\n"):
    address = (host, port)
    sock = socket.socket(family, sock_type)
    sock.connect(address)
    sock.send(request.encode())
    result = sock.recv(4096)
    parser = MyHTMLParser()
    print(parser.feed(result.decode(encoding="ISO-8859-1")))
    sock.close()


socket_connect()
