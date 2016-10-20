from bottle import *

@route("/formy")
@post("/formy")
@view("fm", data = "")
def formy():
    if request.POST.get("submit"):
        val = request.POST.get("val")
        return dict(data = val)
    return dict()

@route("/names-ages")
@view("external", ttl = "Names & Ages")
def names_ages():
    na = [('Lisa', 30), ("John", 21), ("Wanda", None)]
    return dict(na_list = na)

## return template("external", name = name)

@route("/<uid:re:\d{2}>/<name>")
def info(uid, name):
    return template("hello {{uid}}, {{name}}", uid = uid, name = name)

@route("/")
def hello():
    return "<h1>hello</h1> there!"

debug(True)
## by default, host = localhost, port = 8080
## like to input it anyways because it blocks
## auto-incrementing.
run(reloader=True, host="localhost", port=8080)
