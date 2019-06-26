#!/usr/bin/python

import sqlite3
from sqlite3 import Error
import logging
import json


def create_connection(db_file):
    """
    create a database connection to the SQLite database
    specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as connection_error:
        logging.error(connection_error)
    return None


def input_proxy_logs(connection, proxy):
    """
    commit proxy logs to data base
    :param connection: db connection
    :param proxy: proxy logs
    """
    proxy_logs = proxy.har['log']
    cursor = connection.cursor()
    values = (str(proxy_logs['version']), str(proxy_logs['creator']), str(proxy_logs['pages']),
              str(proxy_logs['entries']), str(proxy_logs['comment']))
    cursor.execute('INSERT INTO proxy_logs VALUES (?, ?, ?, ?, ?)', values)
    connection.commit()
    cursor.close()


def main(proxy):
    database = "/home/zhukov/sql/log_base"
    # create a database connection
    connection = create_connection(database)
    with connection:
        logging.info("writing logs into db")
        input_proxy_logs(connection, proxy)
    connection.close()
