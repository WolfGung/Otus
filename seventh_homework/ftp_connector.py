#!/usr/bin/python
# -*- coding: UTF-8 -*-


import ftplib
import logging


class FtpConnector:
    def __init__(self):
        self.address = "127.0.0.1"
        self.path = "Downloads"
        self.directory_name = "MyTestDirectory"
        self.config = {"user": "support",
                       "passwd": "elephant"}

    def connect(self):
        connection = ftplib.FTP(self.address)
        return connection

    def authorize(self, connection):
        connection.login(**self.config)

    def change_directory(self, connection):
        connection.cwd(self.path)

    def create_directory(self, connection):
        connection.mkd(self.directory_name)

    def check_directory(self, connection):
        directory_list = list()
        connection.retrlines("LIST", directory_list.append)
        string = directory_list[0].split()
        if self.directory_name not in string:
            logging.error("There are no directory with name {}".format(self.directory_name))
            raise Warning("There are no directory with name {}".format(self.directory_name))
        else:
            logging.info("Directory with name {} find!".format(self.directory_name))

    def remove_directory(self, connection):
        connection.rmd(self.directory_name)

    @staticmethod
    def close_connection(connection):
        connection.close()
