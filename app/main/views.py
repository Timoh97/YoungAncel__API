from flask import render_template
from . import main

import http.client
from api import api_key

conn = http.client.HTTPSConnection("api-football-beta.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': api_key,
    'X-RapidAPI-Host': "api-football-beta.p.rapidapi.com"
    }

conn.request("GET", "/timezone", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

@main.route('/')
def index():
    return render_template("index.html")