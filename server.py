from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="charles_barkley"
from datetime import datetime
import random

@app.route('/')
def index():
	try:
		session['count']
		session['just_gold']
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
		session['just_gold'] = 0


	return render_template('index.html')


	# return render_template('index.html', count=session['count'], just_gold=session['just_gold'], now=session['now'], casino=session['casino'])

# @app.route('/farm', methods=['POST'])
# def farm_gold():
# 	session['casino'] = 0
# 	session['now'] = datetime.now()
# 	session['just_gold'] += random.randint(10,20) 
# 	session['count'] += session['just_gold']
# 	return redirect('/')

@app.route('/process_money', methods=['POST'])
def process_gold():
	session['now'] = datetime.now()


	if request.form['farm'] ==  'gold_farming':
		session['just_gold'] += random.randint(10,20)
		session['count'] += session['just_gold']
		print request.form['farm']
		
		session['just_gold'] = 0

	if request.form['cave'] == 'gold_caving' :
		session['just_gold'] += random.randint(5,10)
		session['count'] += session['just_gold']

		session['just_gold'] = 0

	if request.form['gold_method'] == session['house']:
		session['just_gold'] += random.randint(2,5)
		session['count'] += session['just_gold']

		session['just_gold'] = 0

	if request.form['gold_method'] == 'gold_casinoing':
		session['count'] += random.randrange(-50,50)
		# if num_gold < 0:
		# 	session['just_gold'] = 
		# 	session['count'] -= session['just_gold']
		# else:
		# 	session['just_gold'] = num_gold
		# 	session['count'] += session['just_gold']

		session['just_gold'] = 0

	return redirect('/')

app.run(debug=True)

