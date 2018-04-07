from flask import Flask, render_template, request, redirect, flash 

app = Flask(__name__)
app.secret_key ="secretsecret"


@app.route('/', methods=['GET'])
def showpage():
	return render_template('survey.html')


@app.route('/result', methods =['POST'])
def create_input():
	name = request.form['yourname']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']

	if len(name) <1:
		flash("NAME CANNOT BE BLANK")
		return redirect('/')

	elif len(comment)<1:
		flash("Comment cannot be blank")
		return redirect('/')

	elif len(comment) >120:
		flash("length cannot exceed 120!")
		return redirect('/')

	else:
		return render_template('result.html', name = name, location = location, language = language, comment =comment)


app.run(debug=True)

 