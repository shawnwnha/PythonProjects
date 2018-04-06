from flask import Flask, render_template, request, redirect 
app = Flask(__name__)

@app.route('/')
def showpage():
	return render_template('survey.html')

@app.route('/result', methods =['POST'])
def create_input():
	name = request.form['yourname']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	return render_template('result.html', name = name, location = location, language = language, comment =comment)


app.run(debug=True)


# , name=name, location=location, language=language, comment=comment

# name = request.form['yourname']
# 	location = request.form['location']
# 	language = request.form['language']
# 	comment = request.form['comment']