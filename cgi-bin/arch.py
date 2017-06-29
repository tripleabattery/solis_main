#!/usr/bin/python3

#TODO: Cleanup, Documentation

from config import mysql, drops
import solis
import os, sys
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()


########################
#    Database Stuff    #
########################
from config import mysql
import MySQLdb
import _mysql_exceptions

try:

    cnx = MySQLdb.connect(mysql["host"], mysql["user"], mysql["pass"], mysql["database"])    # Credentials can be configured in config.py located within the same directory as this file

except MySQLdb.error as err:

    print(err)

else:

    cursor = cnx.cursor()
    sql = drops[form["DROP"].value]["getitems"] # Get items from table `Items`
    sql2 = drops[form["DROP"].value]["geturls"] # Get URL endings

    try:

        cursor.execute(sql2)
        results = cursor.fetchall()



        try:
            cursor.execute(sql.format(form["URL"].value))
            current = cursor.fetchone()

        except:
            cursor.execute(sql.format(results[0][1]))
            current = cursor.fetchone()

        try:
            nextitem = results[current[0]]
        except:
            nextitem = results[0]    # If there is no nextitem, set nextitem to the first item

        try:
            previtem = results[current[0]-2]
        except:
            previtem = results[-1]    # If there is no previtem, set previtem to the last item

    except _mysql_exceptions.MySQLError as err:
        print("<h1>There was an Error:</h1><br>")
        print("<h2>")
        print(err)
        print("</h2></body></html>")

    else:
        try:
            current[0] # Try to index current. Redirect the user if there is an error.
        except:
            print("Location: http://dev.sxlis.com/errors/404.php") #TODO: Make URL configurable from config module
            print("\n\n")
            sys.exit()

        else:
            print("Content-Type: text/html\n\n")
            print(solis.start_html_arch)
            print(solis.html_body_arch.format(title=current[2], desc=current[3], image=current[4], image2=current[5], drop=form["DROP"].value, urlprev=previtem[1], urlnext=nextitem[1]))
            print(solis.end_html_arch)

    cnx.close()
