from logging import _STYLES
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("play.html")

@app.route("/play")
def play1():
    return render_template("play.html", num=3)

@app.route("/play/<int:num>")
def play2(num):
    return render_template("play.html", num=num)

@app.route("/play/<int:num>/<color>")
def play3(num,color):
    return render_template("play.html",num=num, color=color)
    

if __name__ == "__main__":
    app.run(debug=True)
