from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector #SQL connector()
import re #Email regex 
import md5 #hash
import os, binascii #salt

app = Flask(__name__)
SQL = MySQLConnector(app,'practicedb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = "SecretKey"


@app.route('/') ########## LOGIN PAGE 
def login_page():
	return render_template('home.html')

@app.route('/login', methods=['POST']) # send users to main page upon a successful login
def login_post():
	login_id = request.form['id']
	login_pw = request.form['pw']
	query = "select * from users where users.email = :email limit 1"
	data = {'email': login_id}
	
	listed_id = SQL.query_db(query,data)

	if len(login_pw)< 1 or len(login_id)<1:
		flash('Input fields empty')
		return redirect('/')

	else:
		if len(listed_id)!=0:
			encrypted_pw = md5.new(login_pw+listed_id[0]['salt']).hexdigest()
			if listed_id[0]['password'] == encrypted_pw:
				session['user_id'] = listed_id[0]['id'] # session['user_id'] assgined upon a successful login
				print session['user_id']
				return redirect('/main')
			else:
				flash('Wrong password')	
				return redirect('/')

		else:
			flash('Failed to match our records')
			return redirect('/')

################################################################################# REGISTRATION
@app.route('/registration') # show registration form 
def registration_page():
	return render_template('registration.html')


@app.route('/registration/user', methods=['POST']) # send flash and form to SQL database upon a successful registration. 
def registration_post():

	validation = True

	first_name = request.form['first_name'].capitalize()
	last_name = request.form['last_name'].capitalize()
	email = request.form['email'].lower()
	password1 = request.form['password1']
	password2 = request.form['password2']

	if len(first_name)<1 or len(last_name)<1 or len(email)<1 or len(password1)<1 or len(password2)<1: #validate blank  
		flash("Input fields must not have a blank.")
		return redirect('/registration')
	
	else: # validate inputs  
		if not first_name.isalpha() or not last_name.isalpha(): # name alphabet
			flash('Name must be only alphabets.')

		if not EMAIL_REGEX.match(email): # email validation
			flash("Email invalid.")
			validation=False

		if len(password1) <8 or len(password2) <8: # password length 
			flash("Password should be more than 8 characters.")
			validation=False

		if password1 != password2: #password match 
			flash("Password confirmation failed.")
			validation=False

	if validation == False: #show all. 
		return redirect('/registration.')

	else: #validate duplicate email in our system 
		query_findEmail = "select * from users where email = :email"
		data_findEmail = {'email':email}

		email_find = SQL.query_db(query_findEmail,data_findEmail)

		if email_find: 
			flash("We already have email in our system.")
			return redirect('/registration')

		else:# register in system
			salt = binascii.b2a_hex(os.urandom(15))
			encrypted_pw = md5.new(password1+salt).hexdigest()
			query = "insert into users(first_name,last_name,email,password,salt,created_at,updated_at) values(:first_name, :last_name, :email, :password, :salt, now(), now())"
			data = {
				'first_name': first_name,
				'last_name' : last_name,
				'email' : email, 
				'password': encrypted_pw,
				'salt': salt
			}

			SQL.query_db(query,data)
			return redirect('/')

######################################################################################### MAIN
@app.route('/main')
def main():
	if session['user_id']:
		message = SQL.query_db("select messages.id, messages.message, messages.created_at, messages.user_id, concat(users.first_name, ' ',users.last_name) as user_name from messages join users on user_id = users.id order by messages.created_at")
		comment = SQL.query_db("select comments.id, comments.comment, comments.created_at, comments.updated_at, comments.user_id, concat(users.first_name,' ',users.last_name)as user_name,comments.message_id from comments join users on user_id = users.id")
		return render_template('main.html', SQL_messages =message, SQL_comments = comment)
	else:
		return redirect('/')

@app.route('/main/message', methods=['POST']) #send message to SQL database
def message():
	message = request.form['message']
	query = "insert into messages(message, created_at, updated_at, user_id) values(:message, now(), now(), :user_id)"
	data={
		'message': message,
		'user_id': session['user_id'],
	}

	SQL.query_db(query,data)
	return redirect('/main')

@app.route('/main/comment', methods=['POST']) #send comment to SQL database
def comment():
	comment = request.form['comment']
	message_id = request.form['hidden']
	query="insert into comments(comment, created_at, updated_at, user_id, message_id) values(:comment, now(),now(), :user_id, :message_id)"
	data={
		'comment': comment,
		'user_id': session['user_id'],
		'message_id': message_id
	}

	SQL.query_db(query,data)
	return redirect('/main')

@app.route('/main/comment-delete', methods=['POST']) # delete comment from SQL database
def delete_comment():
	comment_id = request.form['hidden']
	query_validate= "select * from comments where comments.id = :comment_id and comments.user_id = :user_id limit 1"
	data_validate = {
		'comment_id': comment_id,
		'user_id': session['user_id']
	}
	comment_validate =SQL.query_db(query_validate,data_validate)

	if len(comment_validate) > 0:
		query="delete from comments where comments.id = :comment_id and comments.user_id = :user_id limit 1"
		data = {
			'comment_id': comment_id, 
			'user_id': session['user_id']
		}

		SQL.query_db(query,data)

	else:
		flash("delete Invalid: you can only delete posts YOU posted!")

	return redirect('/main')
	
	

@app.route('/main/logoff', methods =['GET'])
def logoff():
	session['user_id'] = None
	return redirect('/')


app.run(debug = True)