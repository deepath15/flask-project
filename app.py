from flask import Flask, render_template,request,redirect,url_for
from signupdb import col
from signindb import data
app = Flask(__name__,template_folder="html",static_folder="static")


@app.route("/", methods=["post", "get"])
@app.route("/signin", methods=["post", "get"])
def root():
    global tit
    tit="file not found"
    global mes
    mes=404
 
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        retrivedData=data(username,password)
        print(retrivedData)
        
        if retrivedData!=False:
            tit="home page"
            mes=retrivedData
            return redirect(url_for("home"))

      
    return render_template("index.html")

    
    

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
        
        #data load
        
        col.insert_one({"username":username,"fname":fname,"lname":lname,"email":email,"phone":phone,"password":password,"dob":dob,})
       
        
        return redirect(url_for('root'))
    return render_template('signup.html')

@app.route('/home')
def home():
        return render_template('home.html', title=tit,message=mes)

    
  
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

