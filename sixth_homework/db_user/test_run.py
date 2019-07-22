#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from sixth_homework.db_user.db_connector import SqlTest


def run_test():
    DataBase = SqlTest()
    Connection = DataBase.mysql_connect()
    DataBase.create_table(Connection)
    DataBase.check_table(Connection)
    DataBase.remove_table(Connection)
