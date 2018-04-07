from flask import Flask, render_template, request, redirect, session
a = Flask(__name__)
a.secret_key = "Thisissecret"

@a.route('/')
def firstpage():
	return render_template('index.html')

@a.route('/user', methods =['POST'])
def create_U():
	session['name'] = request.form['name']
	session['email'] = request.form['email']
	return redirect('/show')

@a.route('/show')
def show_user():
	return render_template('user.html')

a.run(debug =True)