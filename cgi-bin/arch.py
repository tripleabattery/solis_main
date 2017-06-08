#!/usr/bin/python3

from config import page, mysql

print("Content-Type: text/html")

########################
#    Database Stuff    #
########################
from config import mysql
import MySQLdb

try:
    cnx = MySQLdb.connect(mysql["host"], mysql["user"], mysql["pass"], mysql["database"])
    
except MySQLdb.error as err:

    print(err)

else:

    cursor = cnx.cursor()
    sql = "SELECT * f" #TODO: Get all items from the Items table
    
    try:

        cursor.execute(sql)

    except _mysql_exceptions.MySQLError as err:
        print("<h1>There was an Error:</h1><br>")
        print("<h2>")
        print(err)
        print("<br>")
        print("</h2></body></html>")

    else:
        print()

    cnx.close()

print(page.format("test", "test", "test"))
