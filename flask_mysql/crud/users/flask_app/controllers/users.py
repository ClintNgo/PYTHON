from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route("/")
def read():
    users = User.get_all_users()
    return render_template("read.html", users=users)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/create/user", methods = ["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.create_user(data)
    return redirect("/user/<int:id>")

@app.route("/user/<int:id>")
def show_user(id):
    data = {
        "id":id
    }
    user = User.get_user(data)
    return render_template("readone.html", user=user)

@app.route("/edit/<int:id>")
def edit_user(id):
    data = {
        "id":id,
    }
    user = User.get_user(data)
    return render_template("edit.html",user=user)

@app.route("/edituser/<int:id>", methods= ["POST"])
def edit_user_db(id):
    data = {
        "id" : id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.edit_user(data)
    return redirect("/user/"+str(id))

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    User.delete_user(data)
    return redirect("/")
