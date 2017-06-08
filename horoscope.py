#!/usr/bin/python3

import sys
import requests

h = input("Enter your horoscope: ")
url = "https://theastrologer-api.herokuapp.com/api/horoscope/"
req = requests.get(url + h + "/today")
r = req.json()

print("Your horoscope for " + r["date"] + " is: ")

print(r["horoscope"])
