#!/usr/bin/python3

from config import page, mysql
import os, sys
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html")

########################
#    Database Stuff    #
########################
from config import mysql
import MySQLdb
import _mysql_exceptions

try:
    cnx = MySQLdb.connect(mysql["host"], mysql["user"], mysql["pass"], mysql["database"])
    
except MySQLdb.error as err:

    print(err)

else:

    cursor = cnx.cursor()
    sql = "SELECT * FROM `Items` WHERE `ID` = {0} " # Get items fro table `Items`
    sql2 = "SELECT `ID` FROM `Items`" # Get ID numbers
    try:

        cursor.execute(sql.format(form["ID"].value))
        current = cursor.fetchone()

        cursor.execute(sql.format(int(form["ID"].value)+1))
        result = cursor.fetchone()
        if result:
            nextitem = result[0]
        else:
            nextitem = 0

        cursor.execute(sql.format(int(form["ID"].value)-1))
        result = cursor.fetchone()
        if result:
            previtem = result[0]
        else:
            previtem = 0

        cursor.execute(sql2)
        numbs = cursor.fetchall()

    except _mysql_exceptions.MySQLError as err:
        print("<h1>There was an Error:</h1><br>")
        print("<h2>")
        print(err)
        print("<br>")
        print("</h2></body></html>")

    else:

        print(page.format(title=current[1], desc=current[2], image=current[3], idprev=previtem, idnext=nextitem))
        print(numbs)
        #TODO:  Fix bug where clicking next/prev on an item that doesn't have a next/prev item causes an error
        #TODO: Allow non-sequential ID numbers

    cnx.close()
