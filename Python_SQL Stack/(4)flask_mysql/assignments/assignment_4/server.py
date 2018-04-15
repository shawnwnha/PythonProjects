from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5 
import os, binascii

validate_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "secretsecretsecret"
mysql = MySQLConnector(app,'walldb')


@app.route('/')
def login():
	return render_template('index.html')

# _________________________________LOGIN_______________________________________ #

@app.route('/user', methods=['POST'])
def login_successful():
	session['user_id'] = request.form['login_id']
	session['user_pw'] = request.form['login_pw']
	query = 'select * from users where users.email = :email limit 1'
	data={
		'email':session['user_id']
	}
	validation = mysql.query_db(query,data)

	if len(validation) != 0:
		encrypted_password = md5.new(session['user_pw'] + validation[0]['salt']).hexdigest()
		if validation[0]['password'] == encrypted_password:
			session['id'] = validation[0]['id']
			print session['id']
			return redirect('/wall')
		else:
			flash('Password does not match with our records', 'password_failed')
			return redirect('/')
	else:
		flash('There is no record of your email & password/ To register, click link below', 'no_records')
		return redirect('/')

# _________________________________Main Page_______________________________________ #



@app.route('/wall')
def main():
	messages = mysql.query_db('select messages.id, messages.message, messages.created_at, users.first_name, users.last_name from messages join users on user_id = users.id order by messages.created_at desc')
	comments = mysql.query_db('select comments.id, comments.comment, comments.created_at, comments.message_id, messages.user_id, concat(users.first_name,users.last_name) as user_name from comments join messages on comments.message_id = messages.id join users on messages.user_id = users.id')
	print comments
	return render_template('user.html', posted_messages=messages, posted_comments=comments)



# _________________________________Submit Message_______________________________________ #
@app.route('/wall/message_process', methods=['POST'])
def post_messages():
	message = request.form['messages']
	query= 'insert into messages (message, created_at, updated_at, user_id) values(:message, now(), now(), :user_id)'
	data={
		'message': message,
		'user_id': session['id']
	}
	message_submit = mysql.query_db(query,data)
	return redirect('/wall')

@app.route('/wall/comment_process', methods=['POST'])
def post_comments():
	comment = request.form['comment']
	message_id = request.form['messages_id'] 
	query = 'insert into comments (comment, created_at, updated_at, user_id, message_id) values(:comment, now(),now(),:user_id,:message_id)'
	data={
		'comment': comment,
		'user_id': session['id'],
		'message_id': message_id
	}

	comment_submit = mysql.query_db(query,data)
	return redirect('/wall')

# _________________________________REGISTER_______________________________________ #

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/register/confirm', methods =['POST'])
def confirm():
	if request.form['hidden'] == 'register':
		errors = False 
		session['first_name'] = request.form['register_fn']
		session['last_name'] = request.form['register_ln']
		session['email'] = request.form['register_email'].lower()
		session['password'] = request.form['register_pw']
		session['password_c'] = request.form['register_pwc']
		# salt = binascii.b2a_hex(os.urandom(15))
		# session['hashed_pw'] = md5.new(session['password'] + salt).hexdigest()

		if len(session['first_name']) < 2 or len(session['last_name']) < 2:
			flash('first and last name should be at least 2 characters')
			errors = True
			print "name length fail"

		if not validate_email.match(session['email']):
			flash('Email not valid','email_invalid')
			errors = True 
			print "email_fail"

		if session['password'] != session['password_c']:
			flash('password confirmation failed','password_confirmation')
			errors = True
			print "password matching fail"

		if len(session['password']) <8 or len(session['password_c']) <8:
			flash('password should be more than 8 characters!','password_length_fail')
			errors = True


		if errors == True:
			return redirect('/register')
			
		else:
			print 'pass'
			flash('You have been successfully registered')
			salt = binascii.b2a_hex(os.urandom(15))
			hashed_pw = md5.new(session['password'] + salt).hexdigest()
			query = 'insert into users (first_name, last_name, email, password, salt, created_at, updated_at) values(:first_name, :last_name, :email, :password, :salt, now(), now())'
			data = {
				'first_name': session['first_name'],
				'last_name' : session['last_name'],
				'email':session['email'],
				'password': hashed_pw,
				'salt': salt,
			}
			mysql.query_db(query,data)
			return redirect('/')

app.run(debug=True)