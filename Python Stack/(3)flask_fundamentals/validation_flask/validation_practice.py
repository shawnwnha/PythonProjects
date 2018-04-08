from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "don'tforgettomakeitsecret"

@app.route('/', methods=['GET'])
def index():
	return render_template(('validation_practice.html'))

@app.route('/process', methods=['POST'])
def process():
	if len(request.form['name']) < 1:
		flash("EMAIL cannot be empty!")
	elif not EMAIL_REGEX.match(request.form['name']):
		flash("INVALID EMAIL")
	else:
		flash("success, you email is {}".format(request.form['name']))

	return redirect ('/')

app.run(debug = True)