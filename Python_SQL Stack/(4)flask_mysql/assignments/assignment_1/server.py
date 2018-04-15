from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')

@app.route('/')
def index():
	friends = mysql.query_db('select first_name, last_name, age, date(created_at) as date, year(created_at) as year from friends')
	return render_template('index.html', all_friends = friends)

@app.route('/friends', methods =['POST'])
def create():
	query = 'insert into friends (first_name, last_name, age, created_at, updated_at) values(:first_name, :last_name, :age, now(),now())'
	data = {
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'age': request.form['age'],
	}

	mysql.query_db(query,data)
	return redirect('/')

# @app.route('/friends/<friend_id>')
# def show(friend_id):
# 	query ="select first_name, last_name, age, date(created_at) as date, year(created_at) as year from friends where id = :specific_id"
# 	data = {
# 		'specific_id':friend_id
# 	}
# 	friends = mysql.query_db(query,data)

# 	return render_template('index.html', one_friend = friends[0])

app.run(debug=True)