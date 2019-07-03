#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


import socket


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
    data = (result.decode(encoding="ISO-8859-1"))
    some_data = (data.split('\n'))
    final_dict = dict()
    for i in some_data:
        new_str = i.split()
        if len(new_str) > 1:
            final_dict[new_str[0]] = new_str[1:]
        else:
            continue
    print(final_dict)
    sock.close()


socket_connect()
