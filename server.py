from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="charles_barkley"
from datetime import datetime
import random

@app.route('/')
def index():
	try:
		session['count']
		session['farm']
		session['cave']
		session['house'] 
		session['casino']

	except:
		session['farm'] = 0
		session['cave'] = 0
		session['house'] = 0
		session['casino'] = 0
		session['count'] = 0


	return render_template('index.html')


	# try:
	# 	session['count']
	# 	session['just_gold']
	# 	session['now'] 
	# 	session['casino']
	# except:
	# 	session['count'] = 0
	# 	session['just_gold'] = 0
	# 	session['now'] = 0
	# 	session['casino'] = 0

	# return render_template('index.html', count=session['count'], just_gold=session['just_gold'], now=session['now'], casino=session['casino'])

# @app.route('/farm', methods=['POST'])
# def farm_gold():
# 	session['casino'] = 0
# 	session['now'] = datetime.now()
# 	session['just_gold'] += random.randint(10,20) 
# 	session['count'] += session['just_gold']
# 	return redirect('/')

@app.route('/process_money' methods=['POST'])
def process_gold():
	session['now'] = datetime.now()
	session['farm'] = request.form['farm']
	session['cave'] = request.form['cave']
	session['house'] = request.form['house']
	session['casino'] = request.form['casino']

	try:
		session['farm']
		session['cave']
		session['house'] 
		session['casino']
	except:
		session['farm'] = 0
		session['cave'] = 0
		session['house'] = 0
		session['casino'] = 0

	if session['farm'] == 1:
		session['just_gold'] += random.randint(10,20)
		session['count'] += session['just_gold']

		session['farm'] == 0

	if session['cave'] = 1:
		session['just_gold'] += random.randint(5,10)
		session['count'] += session['just_gold']

		session['cave'] == 0

	if session['house'] = 1:
		session['just_gold'] = random.randint(2,5)
		session['count'] += session['just_gold']

		session['house'] == 0

	if session['casino'] = 1:
		session['just_gold'] = random.randint()
		num_gold = random.randin(0,50)
		earn_or_take = random.randint(0,1)
		if earn_or_take == 0:
			session['just_gold'] -= num_gold
		else:
			session['just_gold'] += num_gold
		session['count'] += session['just_gold']

		session['casino'] = 0

	return redirect('/')

	app.run(debug=True)

