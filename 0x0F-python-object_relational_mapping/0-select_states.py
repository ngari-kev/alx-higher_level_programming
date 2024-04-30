#!/usr/bin/python3
"""Lists all states entries in a db"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    con = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset='utf8')

    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    entries = cursor.fetchall()

    for entry in entries:
        print(entry)

    cursor.close()
    con.close()
