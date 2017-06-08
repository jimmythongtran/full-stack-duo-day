#!/usr/bin/python3
"""
checks user's horoscope for the day
"""
import requests
h = input("Enter your horoscope: ")
url = "https://theastrologer-api.herokuapp.com/api/horoscope/"
try:
    req = requests.get(url + h.lower() + "/today")
    r = req.json()
    print("Your horoscope for " + r["date"] + " is: ")
    print("Horoscope: " + r["horoscope"])
    print("Intensity: " + r["meta"]["intensity"])
    print("Keywords: " + r["meta"]["keywords"])
    print("Mood: " + r["meta"]["mood"])
except:
    print("Invalid input")
