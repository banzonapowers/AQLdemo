#!/usr/bin/python3
from easy_login import login

username = ""
password = ""
address = ""

object = login(username, password, address)

object.myweb("demouser", "My$3c1D", "https://www.google.com")
