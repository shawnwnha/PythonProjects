from flask import Flask, render_template, request, redirect 

app = Flask(__name__)

@app.route('/')
def landingpage():
	return render_template('submit.html')


@app.route('/process', methods=['POST'])
def process():
	yourname = request.form['yourname']
	print yourname
	return redirect('/')

app.run(debug = True)