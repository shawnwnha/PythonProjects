from flask import Flask, render_template, request, redirect
a = Flask(__name__)

@a.route('/')
def greeting():
	return render_template('dojo.html')

# @a.route('/ninjas')
# def ninja():
# 	return render_template('ninjas.html')

@a.route('/dojo/new', methods=['POST'])
def inputs():
	firstname=request.form['first_name']
	lastname= request.form['last_name']
	return redirect('/')



a.run(debug = True)