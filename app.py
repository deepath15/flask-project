from flask import Flask, render_template
from signin import signIn
from signup import signUp
app = Flask(__name__,template_folder="html",static_folder="static")

@app.route("/", methods=["post", "get"])
def login():
<<<<<<< HEAD
    return signIn()
    
@app.route('/signup', methods=["get"])
=======
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        


    # check if the username and password are correct
        if username == 'deepath' and password =='1':
            # if they are, redirect the user to the home page
            return render_template('home.html')
            
    return render_template("index.html")
@app.route('/signup.html', methods=["get"])
>>>>>>> origin/main
def signup():
    

    return render_template('signup.html')

@app.route('/home',methods=["get"])
def home():
    return render_template('404.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
