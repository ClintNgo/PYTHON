from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo

@app.route("/")
def home():
    dojos_ninjas = Dojo.show_dojo()
    return render_template ("home.html", dojos_ninjas = dojos_ninjas)

@app.route("/create/dojo", methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"] 
    }
    Dojo.create_dojo(data)
    return redirect("/")

@app.route("/dojo")
def dojopage():
    return render_template("dojo.html")

@app.route("/dojo/<int:id>")
def dojo(id):
    data ={
        "id":id
    }
    dojo_ninjas = Dojo.get_dojo_ninjas(data)
    return render_template("dojo.html",dojo_ninjas=dojo_ninjas)

@app.route("/addNinja")
def new():
    dojos_ninjas = Dojo.show_dojo()
    return render_template ("new.html", dojos_ninjas=dojos_ninjas)

@app.route("/create/ninja", methods=["POST"])
def create_ninja():
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    Dojo.create_ninja(data)
    return redirect("/dojo/"+str(request.form["dojo_id"]))
