#!/usr/bin/python3
'''A script that lists all states from the database hbtn_0e_0_usa'''

import MySQLdb
import sys

def list_all():
    '''A function that lists all states from the database'''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306
    conn = MySQLdb.connect(host=host, port=port, user=username, passwd=password, db=db_name, charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    query_rows = cur.fetchall()
    if query_rows:
        for row in query_rows:
            print(row)
    cur.close()
    conn.close()

if __name__ == '__main__':
    list_all()
