from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/dojo/<ninja>")
def ninja_page(ninja):
    print(ninja)
    return f"Hi! {ninja}"

@app.route("/repeat/<number>/<word>")
def repeat_page(number, word):
    word = word * int(number)
    return f"{word}"

@app.errorhandler(404) 
def invalid_route(e): 
    return "Error 404 : Invalid route."

if __name__ == "__main__":
    app.run(debug=True)