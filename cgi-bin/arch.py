#!/usr/bin/python3

#TODO: Cleanup, Documentation

from config import mysql, drops
import solis
import os, sys
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html\n\n")
print(solis.start_html_arch)

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

        cursor.execute(sql.format(form["URL"].value))
        current = cursor.fetchone()

        try:
            currentid = current[0]
        except:
            print("TODO: Make this a 404 page :^)")

        cursor.execute(sql2)
        results = cursor.fetchall()
        sresults = sorted(results)

        for x in sresults:    # loop gets current item's index within the results list then sets currentidindex to this number
            if currentid == x[0]:
                currentidindex = sresults.index(x)
                break


        try:
            nextitem = sresults[currentidindex+1]
        except:
            nextitem = sresults[0]    # If there is no nextitem, set nextitem to the first item

        try:
            previtem = sresults[currentidindex-1]
        except:
            previtem = sresults[-1]    # If there is no previtem, set previtem to the last item

    except _mysql_exceptions.MySQLError as err:
        print("<h1>There was an Error:</h1><br>")
        print("<h2>")
        print(err)
        print("</h2></body></html>")

    else:
        print(solis.html_body_arch.format(title=current[2], desc=current[3], image=current[4], image2=current[5], drop=form["DROP"].value, urlprev=previtem[6], urlnext=nextitem[6]))
        print(solis.end_html_arch)

    cnx.close()
