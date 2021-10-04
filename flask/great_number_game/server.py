from flask import Flask, render_template, request, redirect
from flask.globals import session
from random import randint, random

app = Flask(__name__)
app.secret_key = "Mewtwo"

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/guess", methods = ["POST"])
def guess():
    x = random.randint(0,100)
    guess = int(input("number"))
    if "guess" not in session:
        session["guess"] = guess
    if x == guess:
            session["guess"] = int.input("number") + f"was the right number!"
    elif x > guess:
            session["guess"] = f"Too High!"
    elif x < guess:
            session["guess"] = f"Too low!"
    return render_template("index.html", number=session["guess"])


@app.route("/destroy_session")
def clear():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)