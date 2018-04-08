from flask import Flask, render_template, request, redirect, session 
import random
from datetime import datetime


app = Flask(__name__)
app.secret_key = "secured_password"


now = datetime.now()
print now

@app.route('/')
def show_all():
	session.clear()
	session['log_list'] =[]
	if 'score' not in session:
		session['score'] = 0
	return render_template('gold.html', total_gold = session['score'])

@app.route('/process_money', methods =['POST'])
def processMoney():
	gold = 0
	temp_list=[]
	if request.form['hidden'] == 'farm':
		gold = random.randint(10,20)
	elif request.form['hidden'] == 'cave':
		gold = random.randint(5,10)
	elif request.form['hidden'] == 'house':
		gold = random.randint(2,5)
	elif request.form['hidden'] == 'casino':
		x = random.randint(0,2)
		if x == 0:
			gold = 0
		else:
			gold = 50

	session['score'] += gold
	write_log = "Earned "+ str(gold)+" golds from the farm! "+str(now)
	session['log_list'].append(write_log)

	return render_template('gold.html', total_gold = session['score'])

app.run(debug = True)