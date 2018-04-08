from flask import Flask, render_template, request, redirect 

app = Flask(__name__)

@app.route('/')
def frontpage():
	return "No Ninjas here"

@app.route('/ninja')
def ninjapage():
	return render_template('turtle_main.html')

@app.route('/ninja/<turtle>')
def handler_function(turtle):
		return render_template('turtle.html', name = turtle)

app.run(debug =True)