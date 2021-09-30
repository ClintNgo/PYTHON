from flask import Flask, render_template
import facts 

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/monsters/<monster>")
def monster_page(monster):
    if monster.lower() == "dracula" or monster.lower() == "mummy" or monster.lower() == "frankenstein":
        return render_template("monster.html", monster_name = monster.capitalize(), facts = eval(f"facts.{monster.lower()}_facts"))
if __name__ == "__main__":
    app.run(debug=True)