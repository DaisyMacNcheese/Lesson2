#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    try:
        name = request.args.get('name')
        assert name
    except:
        name = 'Lame! What\'s your name?'
    return render_template('tutorial.html',name=name)


@app.route("/calculate", methods=['GET','POST'])
def calculate():


	#should move this into the if GET but being lazy
	#there is also probably a way to check both the post or get data at once.


	try:
		name = request.args.get('name')
		assert name
	except:
		name = 'Nameless Cyborg'
	try:
		value1 = request.args.get('value1')
		assert value1
	except:
		value1=0
	try:
		value2 = request.args.get('value2')
		assert value2
	except:
		value2=0
	'''

After lots of trial and error I've determined this doesnt work: 
	if isinstance(value1,int) and isinstance(value2,int):
		test='true'
	else:
		test='false'
	'''
	if request.method == 'GET':
		action='addition'
		try:
			result=int(value1)+int(value2)
			return render_template('homework2.html',name=name,value1=value1,value2=value2,action=action,result=result)
		except:
			return render_template('wrong.html',name=name)


	if request.method == 'POST':

		try:
			name = request.form.get('name')
			assert name
		except:
			name = 'POSTed Cyborg'
		try:
			value1 = request.form.get('value1')
			assert value1
		except:
			value1 = 0
		try:
			value2 = request.form.get('value2')
			assert value2
		except:
			value2 = 0

		action='multiplication'
		try:
			result=int(value1)*int(value2)
			return render_template('homework2.html',name=name,value1=value1,value2=value2,action=action,result=result)
		except:
			return render_template('wrong.html',name=name)


if __name__ == "__main__":
	app.debug = True
	app.run()



