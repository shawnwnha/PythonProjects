from flask import Flask, render_template 

a = Flask(__name__)

@a.route('/')
def hellofunction():
	return "welcome to my portfolio, my name is shawn"

@a.route('/projects')
def projects():
	return render_template('aboutme.html')

@a.route('/about')
def about():
	return "this is my about page, i would like to say, hi!"



a.run(debug =True)