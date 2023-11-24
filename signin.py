from flask import Flask,render_template,request,url_for,redirect

app=Flask(__name__,template_folder='html')
def signIn():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        print("usernames:",username,"password:",password)
        if username=="" and password =="":
            return render_template("index.html")

    # check if the username and password are correct
        if username == 'deepath' and password =='1':
            # if they are, redirect the user to the home page
            return render_template('home.html')
            
    return render_template("index.html")