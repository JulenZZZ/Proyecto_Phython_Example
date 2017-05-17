from flask import Flask
from flask import render_template
from flask import request, url_for, redirect



app=Flask(__name__)
app.debug=True
app.config['SECRET_KEY']='secret_key'

@app.route('/')
def index():
    return render_template("index.html")

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

@app.route("/insert_post", methods=['GET'])
def route_insert_post():
    # GET
    post_name = request.args.get('post_name', '')
    author_name = request.args.get('author_name', '')
    descripcion = request.args.get('descripcion','')

    insert_post(post_name ,author_name ,descripcion)
    
    return redirect('/select_all_students')

    
@app.route('/logout')
def logout():
    flash="Acabas de cerrar sesión!"
    return render_template('login.html', flash=flash)

if __name__ == "__main__":
    app.run()
