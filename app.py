from flask import Flask, render_template
from signin import signIn
from signup import signUp
app = Flask(__name__,template_folder="html",static_folder="static")

@app.route("/", methods=["post", "get"])
def login():
    return signIn()
    
@app.route('/signup', methods=["get"])
def signup():
    

    return render_template('signup.html')

@app.route('/home',methods=["get"])
def home():
    return render_template('404.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
