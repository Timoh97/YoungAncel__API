from flask import render_template
from . import main

import http.client
from ..api import api_key
import json



conn = http.client.HTTPSConnection("odds.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': api_key,
    'X-RapidAPI-Host': "odds.p.rapidapi.com"
    }

conn.request("GET", "/v4/sports?all=true", headers=headers)

res = conn.getresponse()
data = res.read()

name=data.decode("utf-8")
conv = json.loads(name)
game=conv


@main.route('/')
def index():
    games={'game':game}
    dictionary=games.values()
    dictionary=dictionary
    
    # print(dictionary) gives list inside a list
    
    return render_template("main/index.html")