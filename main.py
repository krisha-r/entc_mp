from flask import Flask, render_template, request, redirect
import os
from supabase import create_client, Client
from dotenv import load_dotenv
import db

load_dotenv()

app = Flask(__name__)


app.secret_key = "APP_SECRET_KEY"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        username = username.lower()
        password = request.form['password']
        dob = request.form['dob']
        if db.register_user(username, password, dob):
                # If the username and password are added then redirect them to the homepage
                return redirect("/")
        # else:
            # flash("This username is already taken")
    return render_template("register.html"  )
  
@app.route("/login")
def login():
    return render_template("login.html")



if __name__=="__main__":
    app.run(debug=False)
    
