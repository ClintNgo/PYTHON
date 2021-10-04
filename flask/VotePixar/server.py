from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = "shhhhhhhh"

@app.route("/")
def index():
    if "voters" not in session:
        session["voters"] = []
    
    if "votes" not in session:
        session["votes"] = {"total":0,"Toy Story":0,"The Incredibles":0, "Monsters Inc":0}

    return render_template("index.html")

@app.route("/vote", methods=["POST"])
def vote():
    # temp_user = {
    #     "name": request.form["name"],
    #     "age": request.form["age"],
    #     "movie": request.form["movie"]
    # }
    temp_user = {}
    temp_user["name"] = request.form["name"]
    temp_user["age"] = request.form["age"]
    temp_user["movie"] = request.form["movie"]
    session["voters"].append(temp_user)
    # voters = session["voters"]
    # voters.append(temp_user)
    # session["voters"] = voters
    session["votes"]["total"] += 1
    session["votes"][temp_user["movie"]] += 1
    session.modified = True
    return redirect("/results")

@app.route("/results")
def results():
    
    return render_template("results.html",voters=session["voters"])

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")    

if __name__ == "__main__":
    app.run(debug=True)