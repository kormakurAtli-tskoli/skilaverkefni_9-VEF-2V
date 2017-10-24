# Kormákur Atli Unnþórsson
# 10.24.2017
# Skilaverkefni 9

from bottle import *
import json

#static files route
@route("/static/<filename>")
def staticFile(filename):
    return static_file(filename, root="./static/")

@get("/")
def index():
    x = "test"
    with open("static/myndir.json","r") as skra:
        gogn = json.load(skra)
    print(gogn)
    print(gogn["mynd"])
    for i in gogn["mynd"]:
        print(i["title"])
        print(i["link"])
    fjMynda = len(list(gogn["mynd"]))
    listi = gogn["mynd"]
    
    """with open("static/myndir.json","w") as skra:
        gogn[int(big+1)] = x
        json.dump(gogn,skra)
    skra.close()"""
    
    return template("index.tpl",listi = listi)

@post("/vidbot")
def vidbot():
    pass

run()
