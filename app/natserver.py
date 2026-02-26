from datetime import datetime
import os
from flask import Flask, flash, render_template, request, redirect
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def signup():
    if request.method == 'POST': 
        name=request.form['name']
        email=request.form["email"]
        password=request.form['password']
        city=request.form['cities']
        now = datetime.now() 
        dt= now.strftime("%d/%m/%Y %H:%M:%S")
        if (name) in open('users.txt').read():
            print(name)               
            return render_template("signuperror.html")   
        else:
            with open('users.txt','a') as file:
                file.write(f"\n{name}  {email} {password} {city} {dt}")
                file.close()
            return render_template("signup.html")
    else:
        return render_template("signup.html")
        