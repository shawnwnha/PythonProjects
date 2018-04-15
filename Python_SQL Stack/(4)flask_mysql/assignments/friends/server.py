from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
	friends = mysql.query_db('select * from friends')
	print friends 
	return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():

	query = 'insert into friends (first_name, last_name, occupation, created_at, updated_at) values (:first_name, :last_name, :occupation, now(), now())'
	data ={
		'first_name': request.form['first_name'], 
		'last_name': request.form['last_name'], 
		'occupation': request.form['occupation']
	}

	mysql.query_db(query,data)
	return redirect('/')


# @app.route('/friends/<friend_id>')
# def show(friend_id):
# 	query = "insert into friends where id = :specific_id"
# 	data ={'specific_id':friend_id}
# 	friends = mysql.query_db(query,data)

# 	return render_template('index.html', one_friends= friends[0])

app.run(debug=True)