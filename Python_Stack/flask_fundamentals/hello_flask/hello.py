from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def showHello():
	return "Welcome to my portfolio! My name is Shawn, and this is the root route!!!"

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/about')
def aboutme():
	return render_template('aboutme.html')

app.run(debug =True)	