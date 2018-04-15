from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5 
import os, binascii


validate_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "secretsecret"
mysql = MySQLConnector(app,'registrationdb')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users', methods =['POST'])
def create():
	if request.form['hidden'] == 'register':
		errors = False 
		email = request.form['user_email']
		password = request.form['user_pw']
		password_c = request.form['user_pwc']
		first_name = request.form['user_first_name']
		last_name = request.form['user_last_name']
		salt = binascii.b2a_hex(os.urandom(15))
		hashed_pw = md5.new(password + salt).hexdigest()

	elif request.form['hidden'] == 'login':
		session['login_email'] = request.form['login_id']
		login_pw = request.form['login_pw']
		query = 'select * from users where users.email = :email limit 1'
		data={
			'email':session['login_email']
		}
		validation = mysql.query_db(query,data)

		if len(validation) != 0:
			encrypted_password = md5.new(login_pw + validation[0]['salt']).hexdigest()
			if validation[0]['user_pw'] == encrypted_password:
				return render_template('loggedin.html')
			else:
				flash('password does not match with our records', 'password_failed')
				return redirect('/')
		else:
			flash('we do not have a record of your email & password', 'no_records')
			return redirect('/')

	
	if len(email) < 0 or len(password) <0 or len(password_c) < 0 or len(first_name) < 0 or len(last_name) < 0:
		flash('there must be not a blank!','blank_not_allowed')
		errors = True
		print "blank_fail!!!!!!!!!!!!!!"

	if len(first_name) < 2 or len(last_name) < 2:
		flash('first and last name should be at least 2 characters')
		errors = True
		print "name length fail"

	if not validate_email.match(email):
		flash('Email not valid','email_invalid')
		errors = True 
		print "email_fail"

	if password != password_c:
		flash('password confirmation failed','password_confirmation')
		errors = True
		print "password matching fail"

	if len(password) <8 or len(password_c) <8:
		flash('password should be more than 8 characters!','password_length_fail')
		errors = True


	if errors == True:
		return redirect('/')
	else:
		salt = binascii.b2a_hex(os.urandom(15))
		hashed_pw = md5.new(password + salt).hexdigest()
		query = 'insert into users (email, user_pw, salt, first_name, last_name, created_at, updated_at) values(:email, :user_pw, :salt, :first_name, :last_name, now(), now())'
		data = {
			'email':email,
			'user_pw': hashed_pw,
			'salt': salt,
			'first_name': first_name,
			'last_name' : last_name,
		}
		mysql.query_db(query,data)
		return render_template('success.html')
		

app.run(debug=True)
