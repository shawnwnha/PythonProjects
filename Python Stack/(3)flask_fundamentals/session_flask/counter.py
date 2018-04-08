from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)

app.secret_key = "countersecretkey"


@app.before_first_request
def counterOrigin():
	session['counter']= 0

@app.route('/')
def mainpage():
	return render_template('counter.html', counter = session['counter'] )


@app.route('/post', methods=['POST'])
def increment2():
	if request.form['hidden'] == 'increment2':
		session['counter']+=2

	return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
	if request.form['hidden1'] == 'reset':
		session['counter'] =0

	return redirect('/')



app.run(debug = True)