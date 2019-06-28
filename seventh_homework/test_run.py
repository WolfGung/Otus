#!/usr/bin/python
# -*- coding: UTF-8 -*-


from seventh_homework.ftp_connector import FtpConnector
from seventh_homework.ssh_connector import SshConnector


def ftp_create_directory_test():
    ftp = FtpConnector()
    connection = ftp.connect()
    ftp.authorize(connection)
    ftp.change_directory(connection)
    ftp.create_directory(connection)
    ftp.check_directory(connection)
    ftp.remove_directory(connection)
    ftp.close_connection(connection)


def mysql_restart():
    ssh = SshConnector()
    client = ssh.connection()
    ssh.mysql_restart(client)
    ssh.mysql_check(client)
    ssh.close_client(client)


def apache_restart():
    ssh = SshConnector()
    client = ssh.connection()
    ssh.apache_restart(client)
    ssh.apache_check(client)
    ssh.close_client(client)
