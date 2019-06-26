import psycopg2
from psycopg2 import sql


def main():
    conn = psycopg2.connect(dbname="opencart", user="support",
                            password="elephant", host="localhost")
    # cursor = conn.cursor()
    # cursor.execute('SELECT * FROM opencart.oc_address')
    # record = cursor.fetchone()
    # print(record)
    # cursor.close()
    # conn.close()
