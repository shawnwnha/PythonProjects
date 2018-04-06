from flask import Flask, render_template, request, redirect, session 
import random

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def mainpage():
	if 'random' not in session:
		session['random'] = random.randint(0,100)

	return render_template('GreatNumber.html')


@app.route('/number', methods = ['POST'])
def inputnumber():
	session['playernumber'] = int(request.form['number']) # int prenthesis has been formatted since, input type text always returns value as a string!!!!!!
	print session['playernumber'], session['random']

	if session['playernumber'] == session['random']:
		session['random'] = random.randint(0,100)
		result = "you're right!!! GOOD JOB! IF you want to play more, just input value again"
		return render_template('GreatNumber.html', playagain= result)

	elif session['playernumber'] > session['random']:
		result  = "that's too high"
		return render_template('GreatNumber.html', value = result)

	elif session['playernumber'] < session['random']:
		result = "that's too low"	
		return render_template('GreatNumber.html', value = result)


app.run(debug=True)