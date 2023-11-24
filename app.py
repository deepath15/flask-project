from flask import Flask, request, redirect, render_template, url_for,flash
app = Flask(__name__,template_folder="html",static_folder="style")

@app.route("/", methods=["post", "get"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        print("username:",username,"password:",password)
        if username=="" and password =="":
            return render_template("index.html")

    # check if the username and password are correct
        if username == 'deepath' and password =='1':
            # if they are, redirect the user to the home page
            return render_template('home.html')
            
    return render_template("index.html")
@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)