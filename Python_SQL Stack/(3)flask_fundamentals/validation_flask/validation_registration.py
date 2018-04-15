from flask import Flask, render_template, request, redirect, session, flash
import re

validate_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'

app = Flask(__name__)
app.secret_key = "Secret"

@app.route('/',methods =['GET'])
def registration():
	return render_template('user.html')

@app.route('/user', methods =['POST'])
def userinput():
	errors = False
	email = request.form['email']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	password = request.form['password']
	password_confirmation= request.form['password_c']

	if len(email) < 1 or len(first_name) < 1 or len(last_name) < 1 or len(password) < 1 or len(password_confirmation) < 1: 
		flash('there must be not a blank!','blank_not_allowed')
		errors = True
		print "blank_fail!!!!!!!!!!!!!!"

	if first_name.isalpha() == False or last_name.isalpha() == False:
		flash('Name must be only chracters', 'name_character')
		errors = True 
		print "name_fail!!!!!!!!!!!!!!!!!!!!!"

	if not validate_email.match(email):
		flash('Email not valid','email_invalid')
		errors = True 
		print "email_fail"

	if password != password_confirmation:
		flash('password confirmation failed','password_confirmation')
		errors = True
		print "password matching fail"

	if len(password) <8 or len(password_confirmation) <8:
		flash('password should be more than 8 characters!','password_length_fail')
		errors = True
	
	count = 0 
	for k in password:
		if k.isupper()==True:
			count+=1
	if count == 0:
		errors =True
		flash('password should contain at least 1 uppercase','no_upper')

		
	if errors == True:
		return redirect('/')

	else:
		session['email'] = email
		session['first_name'] = first_name
		session['last_name'] = last_name
		session['password'] = password
		session['password_confirmation'] = password_confirmation
		print "no error"
		return render_template('result.html', name_f = session['first_name'], name_l = session['last_name'], email=session['email'],password=session['password'])

app.run(debug=True)
