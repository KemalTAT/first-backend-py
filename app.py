from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)                                   
def get_db():
  conn = sqlite3.connect("users.db")
  db = conn.cursor()
  db.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT)")
  return db, conn

@app.route("/")
def index():
  return "first backend"

@app.route("/hello")
def hello():
  name = request.args.get("name","world")
  return "hello " + name

@app.route("/login", methods=["GET","POST"])
def login():
  if request.method == "POST":
    name = request.form.get("name")
    db,conn = get_db()
    db.execute("INSERT INTO users (name) VALUES (?)"
,(name,))
    conn.commit()
    conn.close()
    return render_template("login.html",s="add the name")
  else:
    return render_template("login.html",s="")

if __name__ = "__main__":
  app.run(host="0.0.0.0", port=5000)
