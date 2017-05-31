from flask import Flask
from flask import render_template
from flask import request, url_for, redirect
from datetime import datetime

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
    now = datetime.now()
    posts= consulta_all_post()
    msg_inicio_sesion="Estas conectado como ADMIN!!"
    return render_template("home.html",posts=posts, now=now, msg_inicio_sesion=inicio)

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
#funcion para borrar post en desarrollo
@app.route('/delete_post', methods=['GET'])
def delete():
    name_borrar = request.args.get('delete', '')
    
    delete_post(name_borrar)

    return redirect(url_for('home'))

@app.route('/search_post', methods=['GET'])
def search():
    name_buscar = request.args.get('search','')
    posts = search_post(name_buscar)

    return render_template("home.html",posts=posts)

if __name__ == "__main__":
    app.run()









