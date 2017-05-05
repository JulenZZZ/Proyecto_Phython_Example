from flask import Flask , request , abort , redirect , Response ,url_for
from flask.ext.login import LoginManager , login_required , UserMixin , login_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)
app.debug=True

class User(UserMixin):
	def __init__(self , username , password , id , activo=True):
		self.id = id
		self.username = username
		self.password = password
		self.activo = activo

	def get_id(self):
		return self.id
	
	def esta_activado(self):
		return self.activo

	def get_autentificacion(self):
		return make_secure_token(self.username , key='secret_key')

class UsersRepository:
	
	def __init__(self):
		self.users = dict()
		self.users_id_dict = dict()
		self.identifier = 0

	def save_user(self , user):
		self.users_id_dict.setdefault(user.id , user)
		self.users.setdefault(user.username , user)

	def get_user(self , username):
		return self.users.get(username)

	def get_user_by_id(self , userid):
		return self.users.get(userid)

	def next_index(self):
		self.identifier +=1
		return self.identifier

users_repository = UsersRepository()



@app.route('/home')
@login_required
def home():
	return "<h1>User Home</h1>"

@app.route('/login' , methods=['GET' , 'POST'])
def login():
	url_for('static', filename='login_style.css')
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		registeredUser = users_repository.get_user(username)
		print('Users '+ str(users_repository.users))
		print('Register user %s , password %s' % (registeredUser.username, registeredUser.password))
		if registeredUser != None and registeredUser.password == password:
			print('Logged in..')
			login_user(registeredUser)
			return redirect(url_for('home'))
		else:
			return Response('<p>Login failed</p>')
	else:
		pass





# recargar el objeto user      
@login_manager.user_loader
def load_user(userid):
    return users_repository.get_user_by_id(userid)
 
if __name__ == '__main__':
	app.run( debug =True)
