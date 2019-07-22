#!/usr/bin/python
# -*- coding: UTF-8 -*-


import paramiko
from time import sleep


class SshConnector:
    def __init__(self):
        self.config = {"hostname": "192.168.102.98",
                       "username": "support",
                       "password": "elephant",
                       "port": "22"}
        self.mysql_service = "mysql"
        self.apache_service = "apache2"

    def connection(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(**self.config)
        return client

    @staticmethod
    def service_status_check(client, service):
        stdin, stdout, stderr = client.exec_command("service --status-all | grep {}".format(service))
        sleep(5)
        print(stderr.read(), stdin.read())
        data = stdout.read().split()
        return data

    @staticmethod
    def service_restart(client, service):
        stdin, stdout, stderr = client.exec_command("service {} restart".format(service))
        sleep(5)
        print(stderr.read(), stdin.read(), stdout.read())

    def mysql_check(self, client):
        data = SshConnector.service_status_check(client, self.mysql_service)
        if data[1] is not "+":
            raise ValueError("Mysql service status is {}".format(data[1]))

    def apache_check(self, client):
        data = SshConnector.service_status_check(client, self.apache_check)
        if data[1] is not "+":
            raise ValueError("Apache2 service status is {}".format(data[1]))

    def mysql_restart(self, client):
        SshConnector.service_restart(client, self.mysql_service)

    def apache_restart(self, client):
        SshConnector.service_restart(client, self.apache_service)

    @staticmethod
    def close_client(client):
        client.close()
