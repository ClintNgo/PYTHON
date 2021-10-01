from logging import _STYLES
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("checkerboard.html",width=4,height=4)

@app.route("/4")
def checker1():
    return render_template("checkerboard.html", width=2, height=4)


@app.route("/<int:width>/<int:height>")
def checker2(width,height):
    return render_template("checkerboard.html", width=int(width/2), height=int(height/2))

@app.route("/<int:width>/<int:height>/<color1>/<color2>")
def checker3(width,height,color1,color2):
    return render_template("checkerboard.html", width=int(width/2), height=int(height/2), color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)
    