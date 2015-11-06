from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="charles_barkley"

@app.route('/')
def index():
	try:
		session['count']
		session['just_gold'] 
	except:
		session['count'] = 0
		session['just_gold'] = 0
	

	return render_template('index.html', count=session['count'], just_gold=session['just_gold'] )

@app.route('/farm', methods=['POST'])
def farm_gold():
	session['just_gold'] = 0
	x = [10,20]
	import random
	session['just_gold'] += random.randrange(x[0],x[1]) 
	session['count'] += session['just_gold']
	return redirect('/')


@app.route('/cave', methods=['POST'])
def cave_gold():
	session['just_gold'] = 0
	x = [5,10]
	import random
	session['just_gold'] = random.randrange(x[0],x[1])
	session['count'] += session['just_gold']
	return redirect('/')

@app.route('/house', methods=['POST'])
def house_gold():
	session['just_gold'] = 0
	x = [2,5]
	import random
	session['just_gold'] = random.randrange(x[0],x[1])
	session['count'] += session['just_gold'] 
	return redirect('/')

@app.route('/casino', methods=['POST'])
def casino_gold():
	session['just_gold'] = 0
	x = [0,50]
	y = [0,1]
	earn_or_take = 0
	num_gold = 0
	import random
	num_gold = random.randrange(x[0],x[1])
	earn_or_take = random.randrange(y[0],y[1])
	if earn_or_take == 0:
		session['just_gold'] -= num_gold
	else:
		session['just_gold'] += num_gold
	session['count'] += session['just_gold']
	return redirect('/')


app.run(debug=True) 