from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="charles_barkley"

@app.route('/')
def index():
	try:
		session['count']
		session['just_gold']
		session['now'] 
		session['casino']
	except:
		session['count'] = 0
		session['just_gold'] = 0
		session['now'] = 0
		session['casino'] = 0
	

	return render_template('index.html', count=session['count'], just_gold=session['just_gold'], now=session['now'], casino=session['casino'])

@app.route('/farm', methods=['POST'])
def farm_gold():
	session['now'] = 0
	session['casino'] = 0
	from datetime import datetime
	session['now'] = datetime.now()
	session['just_gold'] = 0
	import random
	session['just_gold'] += random.randint(10,20) 
	session['count'] += session['just_gold']
	return redirect('/')


@app.route('/cave', methods=['POST'])
def cave_gold():
	session['now'] = 0
	session['casino'] = 0
	from datetime import datetime
	session['now'] = datetime.now()
	session['just_gold'] = 0
	import random
	session['just_gold'] = random.randint(5,10)
	session['count'] += session['just_gold']
	return redirect('/')

@app.route('/house', methods=['POST'])
def house_gold():
	session['casino'] = 0
	session['now'] = 0
	from datetime import datetime
	session['now'] = datetime.now()
	session['just_gold'] = 0
	import random
	session['just_gold'] = random.randint(2,5)
	session['count'] += session['just_gold'] 
	return redirect('/')

@app.route('/casino', methods=['POST'])
def casino_gold():
	session['casino'] = 1
	session['now'] = 0
	from datetime import datetime
	session['now'] = datetime.now()
	session['just_gold'] = 0
	earn_or_take = 0
	num_gold = 0
	import random
	num_gold = random.randint(0,50)
	earn_or_take = random.randint(0,1)
	if earn_or_take == 0:
		session['just_gold'] -= num_gold
	else:
		session['just_gold'] += num_gold
	session['count'] += session['just_gold']
	return redirect('/')



app.run(debug=True) 