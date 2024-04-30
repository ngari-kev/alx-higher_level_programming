#!/usr/bin/python3
'''Prints all states entries starting with N'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    con = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset='utf8')

    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    entries = cursor.fetchall()

    for entry in entries:
        if entry[1].startswith('N'):
            print(entry)

    cursor.close()
    con.close()
