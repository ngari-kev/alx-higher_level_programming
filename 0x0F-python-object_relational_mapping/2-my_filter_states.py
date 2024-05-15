#!/usr/bin/python3
'''Prints all states entries with name as input'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    con = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset='utf8')

    cursor = con.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s".format(argv[4])
    cursor.execute(query)

    entries = cursor.fetchall()

    for entry in entries:
        print(entry)

    cursor.close()
    con.close()
