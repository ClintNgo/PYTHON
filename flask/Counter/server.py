from flask import Flask, render_template,request, redirect,session
from flask.globals import session
app = Flask(__name__)
app.secret_key = "Fruit Ninja"


@app.route("/")
def visit():
    if "counts" not in session:
        session["counts"] = 0
    if "visit" not in session:
        session["visit"] = 0
    session["visit"] += 1
    session["counts"] += 1
    return render_template("index.html", visit=session["visit"], number=session["counts"])

@app.route("/click")
def count():
    session["counts"] += 1
    session["visit"] -= 1
    return redirect("/")

@app.route("/custom", methods=["POST"])
def custom():
    name = request.form["number"]
    session["counts"] += int(name)
    session["counts"] -= 1
    session["visit"] -= 1
    return redirect("/")

@app.route("/destroy_session")
def clear():
    session.clear() 
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)