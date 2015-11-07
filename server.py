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
		session['now'] 
		session['message']
	except:
		session['count'] = 0
		session['just_gold'] = 0
		session['now'] = 0
		session['message'] = []
	

	return render_template('index.html', count=session['count'], message=session['message'])

@app.route('/farm', methods=['POST'])
def farm_gold():
	session['just_gold'] = 0

	session['now'] = datetime.now()
	session['just_gold'] += random.randint(10,20) 
	session['count'] += session['just_gold']
	session['message'].append('Earned %s gold from the farm! %s' % (session['just_gold'], session['now']))
	return redirect('/')


@app.route('/cave', methods=['POST'])
def cave_gold():
	session['now'] = 0
	
	session['now'] = datetime.now()
	session['just_gold'] = 0
	session['just_gold'] = random.randint(5,10)
	session['count'] += session['just_gold']
	session['message'].append('Earned %s gold from the cave! %s' % (session['just_gold'], session['now']))
	return redirect('/')

@app.route('/house', methods=['POST'])
def house_gold():

	session['now'] = 0
	session['now'] = datetime.now()
	session['just_gold'] = 0
	session['just_gold'] = random.randint(2,5)
	session['count'] += session['just_gold'] 
	session['message'].append('Earned %s gold from the house! %s' % (session['just_gold'], session['now']))
	return redirect('/')

@app.route('/casino', methods=['POST'])
def casino_gold():

	session['now'] = 0
	session['now'] = datetime.now()
	session['just_gold'] = 0
	earn_or_take = 0
	num_gold = 0
	num_gold = random.randint(0,50)
	earn_or_take = random.randint(0,1)
	if earn_or_take == 0:
		session['just_gold'] -= num_gold
		session['message'].append('Entered a casino and lost %s gold! %s' % (session['just_gold'], session['now']))
	else:
		session['just_gold'] += num_gold
		session['message'].append('Entered a casino and gained %s gold! %s' % (session['just_gold'], session['now']))
	session['count'] += session['just_gold']
	return redirect('/')




app.run(debug=True) 
