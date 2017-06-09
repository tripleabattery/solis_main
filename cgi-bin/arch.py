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
    try:
        #print(form)

        cursor.execute(sql.format(form["ID"].value))
        current = cursor.fetchone()

        cursor.execute(sql.format(int(form["ID"].value)+1))
        nextitem = cursor.fetchone()

        cursor.execute(sql.format(int(form["ID"].value)-1))
        previtem = cursor.fetchone()

    except _mysql_exceptions.MySQLError as err:
        print("<h1>There was an Error:</h1><br>")
        print("<h2>")
        print(err)
        print("<br>")
        print("</h2></body></html>")

    else:

        print(page.format(title=current[1], desc=current[2], image=current[3], idprev=previtem[0], idnext=nextitem[0]))
        #TODO:  Fix bug where clicking next sends the user to an item that doesn't exist

    cnx.close()
