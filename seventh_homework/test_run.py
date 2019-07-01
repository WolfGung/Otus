#!/usr/bin/python
# -*- coding: UTF-8 -*-


from seventh_homework.ftp_connector import FtpConnector
from seventh_homework.ssh_connector import SshConnector
import pytest
import logging
import allure


@allure.title("001 Critical: Creating new directory on ftp server")
@allure.severity("critical")
@pytest.mark("FTP")
def test001():
    """
    Test type - positive
    Add new directory
    """
    with allure.step("Connecting to ftp server"):
        ftp = FtpConnector()
        connection = ftp.connect()
    try:
        with allure.step("Authorizing"):
            ftp.authorize(connection)
            logging.debug(ftp.authorize(connection))
        with allure.step("Changing directory"):
            ftp.change_directory(connection)
        with allure.step("Creating directory"):
            ftp.create_directory(connection)
        with allure.step("Checking directory"):
            ftp.check_directory(connection)
    finally:
        with allure.step("Removing directory and disconnect from ftp server"):
            ftp.remove_directory(connection)
            ftp.close_connection(connection)


@allure.title("002 Critical: Restart mysql server")
@allure.severity("critical")
@pytest.mark("opencart")
def test002():
    """
    Test type - positive
    Restart mysql server
    """
    with allure.step("Connecting to remote zone"):
        ssh = SshConnector()
        client = ssh.connection()
        logging.debug(ssh.config)
    try:
        with allure.step("Restarting service"):
            ssh.mysql_restart(client)
        with allure.step("Checking mysql service status"):
            ssh.mysql_check(client)
    finally:
        ssh.close_client(client)


@allure.title("003 Critical: Restart apache service")
@allure.severity("critical")
@pytest.mark("opencart")
def test003():
    """
    Test type - positive
    Restart apache2 service
    """
    with allure.step("Connecting to remote zone"):
        ssh = SshConnector()
        client = ssh.connection()
        logging.debug(ssh.config)
    try:
        with allure.step("Restarting service"):
            ssh.apache_restart(client)
        with allure.step("Checking apache2 service status"):
            ssh.apache_check(client)
    finally:
        ssh.close_client(client)
