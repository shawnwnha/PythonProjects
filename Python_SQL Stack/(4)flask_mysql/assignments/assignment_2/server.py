from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

validate_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "secretsecret"
mysql = MySQLConnector(app,'emaildb')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/emails', methods =['POST'])
def create():
	email= request.form['email']

	if not validate_email.match(email):
		flash('Email not valid','email_invalid')
		print "email_fail"
		return redirect('/')
	else:
		query ="insert into emails(email, created_at, updated_at) values(:email, now(),now())"
		data = {
			'email': email 
		}
		mysql.query_db(query,data)
		emails = mysql.query_db('select email, date(created_at) as date, time(created_at) as time from emails')
		flash('Success you have made a successful entry','email_valid')
		return render_template('success.html', valid_emails = emails)


# def delete():
# 	query ="delete from emails where id= :id"
# 	data = {
# 		'id' :  'max(id) from emails' 
# 	}

# 	mysql.query_db(query,data)
# 	print mysql.query_db(query,data)

app.run(debug=True)	