#!/usr/bin/env python3
import os
import cgi
import cgitb
cgitb.enable()  


import json
from html import escape
import secret
from templates import login_page, secret_page, after_login_incorrect
from http.cookies import SimpleCookie


s = cgi.FieldStorage() 
username = s.getfirst("username")
password = s.getfirst("password")

form_ok = username == secret.username and password == secret.password
print("Content-Type: text/html")
print()

c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = None
c_password = None

if c.get("username"):
    c_username = c.get("username").value
if c.get("password"):
    c_password = c.get("password").value

cookie_ok = c_username == secret.username and c_password == secret.password
# check if the cookie in side return boolean 
if cookie_ok:
    username = c_username
    password = c_password

# if form_ok:
    # print("set-cookie username = ", username)
    # print("set-cookie password = ", password)


print()
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())
    print("inside the else")
    # print("username = :", username)
    # print("password = :", password)