from flask import Flask
from flask import render_template
from flask import request, url_for, redirect

app=Flask(__name__)
app.debug=True

@app.route('/')
def index():
    return "Hola Mundo"

@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error= "Login Failed. El usuario o la contraseña es incorrecta."
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run()
