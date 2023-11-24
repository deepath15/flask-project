from flask import Flask, render_template,request,redirect,url_for
from signin import signIn
app = Flask(__name__,template_folder="html",static_folder="static")

@app.route("/", methods=["post", "get"])
def login():
    return signIn()
    

@app.route('/signup',methods=["post", "get"])
def signUp():
    if request.method=="POST":
        username=request.form['username']
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        phone=request.form['phone']
        dob=request.form['dob']
        password=request.form['password']
        cpassword=request.form['cpassword']
        print(username)
        print(fname)
        print(lname)
        print(email)
        print(phone)
        print(dob)
        print(password)
        print(cpassword)
    return render_template('signup.html',)

@app.route('/home',methods=["get"])
def home():
    return render_template('404.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
