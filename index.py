# Kormákur Atli Unnþórsson
# 10.24.2017
# Skilaverkefni 9

from bottle import *
import json, urllib.request

#static files route
@route("/static/<filename>")
def staticFile(filename):
    return static_file(filename, root="./static/")

@get("/")
def index():
    with open("static/myndir.json","r") as skra:
        gogn = json.load(skra)
    listi = gogn["mynd"]
    return template("index.tpl",listi = listi)

@post("/vidbot")
def vidbot():
    x = request.forms.get("title")
    y = request.forms.get("link")
    with open("static/myndir.json","r") as skra:
        gogn = json.load(skra)
        print(gogn["mynd"])
        gogn["mynd"].append({"title":x,"link":y})
    with open("static/myndir.json","w") as skra:
        json.dump(gogn,skra)
    listi = gogn["mynd"]
    return template("index.tpl",listi = listi)

@route("/concerts")
def index():
    with urllib.request.urlopen("http://www.apis.is/concerts") as skra:
        gogn = json.loads(skra.read().decode())
    listi = gogn["results"]
    return template("concerts.tpl",listi = listi)

run()
