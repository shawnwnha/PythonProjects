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
		index = 0
		return render_template('GreatNumber.html', playagain= result, div = index)

	elif session['playernumber'] > session['random']:
		result  = "that's too high"
		index = 1
		return render_template('GreatNumber.html', value = result, div = index)

	elif session['playernumber'] < session['random']:
		result = "that's too low"	
		index = 2
		return render_template('GreatNumber.html', value = result, div =index)


app.run(debug=True)