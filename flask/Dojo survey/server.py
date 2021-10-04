from flask import Flask, app, render_template, redirect, request, session
app = Flask (__name__)
app.secret_key = "Pikachu"

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/input", methods = ["POST"])
def input():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["favorite"] = request.form["favorite"]
    session["comment"] = request.form["comment"]
    return redirect("/result")

@app.route("/result")
def results():
    return render_template("result.html", name = session["name"], location =session["location"], favorite = session["favorite"], comment = session["comment"])

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")  

if __name__ == "__main__":
    app.run(debug=True)