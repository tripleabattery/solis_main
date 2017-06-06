#!/usr/bin/python3

import cgi

form = cgi.FieldStorage()
print("Content-Type: text/html\n\n")
print("""
<!DOCTYPE html>
<html>
""")
print("<h1>Test:", form["test"].value, "</h1>")
print("</html>")
