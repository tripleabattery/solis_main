#!/usr/bin/python3

from config import page, mysql
import os, sys
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html\n\n")

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
    sql = "SELECT * FROM `Items` WHERE `URL` = '{0}' " # Get items fro table `Items`
    sql2 = "SELECT `URL` FROM `Items`" # Get ID numbers
    try:

        cursor.execute(sql.format(form["URL"].value))
        result = cursor.fetchone()
        current = result
        currentid = result[4]

        cursor.execute(sql2)
        results = cursor.fetchall()
        for x in results:
            if currentid == x[0]:
                print
                currentidindex = results.index(x)
                break

        #print(results)

        try:
            nextitem = results[currentidindex+1]
        except:
            nextitem = results[0]

        try:
            previtem = results[currentidindex-1]
        except:
            previtem = results[-1]

    except _mysql_exceptions.MySQLError as err:
        print("<h1>There was an Error:</h1><br>")
        print("<h2>")
        print(err)
        print("<br>")
        print("</h2></body></html>")

    else:

        print(page.format(title=current[1], desc=current[2], image=current[3], idprev=previtem[0], idnext=nextitem[0]))

    cnx.close()
