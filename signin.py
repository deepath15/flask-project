from flask import Flask,render_template,request,url_for,redirect
from app import home
from signindb import data
app=Flask(__name__,template_folder='html')
def signIn():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        retrivedData=data(username,password)
        for i in  retrivedData:
            print(i)
        if username == 'deepath' and password =='1':
            return redirect(url_for('home'))
        elif username=="" and password =="":
            return render_template("index.html")
            
    return render_template("index.html")
