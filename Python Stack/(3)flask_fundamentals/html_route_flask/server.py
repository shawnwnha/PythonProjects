from flask import Flask, render_template

a =Flask(__name__)

@a.route('/')
def index():
	return render_template('user.html', name ="shawn", email = "google.com", times= 10)

a.run(debug = True)