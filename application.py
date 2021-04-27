"""
    This program creates a sqlite database connection which allows users to interact with a simple webapp request form. 
    by Margarita Cortez-Modell
"""
import sqlite3
from flask import Flask, redirect, url_for, render_template, request, g

app = Flask(__name__)

# connect application path to database
def connect_db():
    sql = sqlite3.connect("./dbhello.db")
    sql.row_factory = sqlite3.Row # this returns tuples when accessing columns
    return sql

# check if the database exists using g("global object")
def get_db():
    if not hasattr(g, "sqlite3"):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

# auto-close the connection to avoid memory leaks
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "sqlite_db"):
        g.sqlite3_db.close()

# What's the MVC - "Submit Name"
    # Model: allows user to submit their name into db
    # View: simple submit form for user to type name into
    # Controller: When name is added to db, "Hello, (name)!" is displayed

# create index with GET and POST 
@app.route("/", methods=["POST", "GET"])
def index():
    # when POST, enter user form data into db
    if request.method == "POST":
        user = request.form["name"]
        # try to access db & allow controller to submit name, otherwise throw error exception. 
        try:
            db = get_db()
            db.execute("INSERT INTO users(name) VALUES (?)", (user,))
            db.commit()
        except:
            return f"<h1> Error: Entry not submitted to database.</h1>"
        # if POST successful, display  user method
        return redirect(url_for("user", usr=user))
    # when GET, display index template
    else:
        return render_template("index.html")

# create user method to say "hello" to user
@app.route("/<usr>")
def user(usr):
    return f"<h1> Hello, {usr}!</h1>"

# run the app
if __name__ == "__main__":
    app.run(debug=True)





