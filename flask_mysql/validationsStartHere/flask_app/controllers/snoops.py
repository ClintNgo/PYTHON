from flask_app import app
from flask import render_template, request, redirect,session,flash
from flask_app.models.snoop import Snoop

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validatevictim", methods=["POST"])
def validate_victim():
    if Snoop.validate_victim(request.form):
        # DB call here ie. Snoop.insert_user(data)
        return redirect("/success")
    else:
        return redirect("/")

@app.route("/success")
def success():
    return render_template("success.html")
