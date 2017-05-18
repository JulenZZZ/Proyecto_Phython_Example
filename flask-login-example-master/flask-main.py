from flask import Flask
from flask import render_template
from flask import request, url_for, redirect

from database import *


app=Flask(__name__)
app.debug=True
app.config['SECRET_KEY']='secret_key'

create_db()
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    posts= consulta_all_post()
    return render_template("home.html",posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error= "Login Failed. El usuario o la contraseña es incorrecta."
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route("/insert_post", methods=['GET'])
def route_insert_post():
    # GET
    post_name = request.args.get('post_name', '')
    author_name = request.args.get('author_name', '')
    descripcion = request.args.get('descripcion','')
    imagen = request.args.get('imagen','')

    insert_post(post_name ,author_name ,descripcion,imagen)
    
    return redirect(url_for('home'))
    #return render_template("home.html", post_name=post_name, author_name=author_name, descripcion=descripcion)

    
@app.route('/logout')
def logout():
    flash="Acabas de cerrar sesión!"
    return render_template('login.html', flash=flash)



if __name__ == "__main__":
    app.run()









#la parte mas importante es el python
#pueden haber funciones que sean por terminal
