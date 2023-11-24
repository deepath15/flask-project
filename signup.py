from flask import Flask,request,redirect,render_template,url_for

app=Flask(__name__,template_folder='html')

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
    return redirect(url_for('/'))
