from flask import (Flask, g, render_template, flash, redirect, url_for)
from flask import json, jsonify, request
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import LoginManager, login_user

import forms
import models
import json
import httplib
import urllib

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
parse_app_id = "cNTa6H9mCY9DG0gk6o3CoBRWrnfrGj7T9OGIdahr"
parse_app_key = "XC9bz01MpdHcOWDpVX7btFeRK1Xf6ThlxWTuVqd4"
app.secret_key = 'sldkjsgifodji2o54389dxnkcklkefer'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

@login_manager.user_loader
def load_user(userid):
	try:
		return models.User.get(models.User.id == userid)
	#error from peewee
	except models.DoesNotExist:
		return None

	
@app.route('/register', methods=('GET', 'POST'))
def register():
	form = forms.RegisterForm()
	if form.validate_on_submit():	
	    username = form.username.data
	    password = form.password.data
	    email = form.email.data
	    
	    connection = httplib.HTTPSConnection('api.parse.com', 443)
	    connection.connect()
	    connection.request('POST', '/1/users', json.dumps({
	        "username": username,
	        "password": password,
	        "email": email,
	        "emailVerification": "false"
	    }), {
	        "X-Parse-Application-Id": parse_app_id,
	        "X-Parse-REST-API-Key": parse_app_key,
	        "Content-Type": "application/json"
	    })
	    result = json.loads(connection.getresponse().read())
	    try:
	        sess_dict = {"id": result['sessionToken'], "objectId": result['objectId']}
	    except KeyError:
	        return jsonify(**result), 400
	    return jsonify(**sess_dict), 201
		#return redirect(url_for('index'))
	return render_template('register.html', form = form)
	
@app.route('/login', methods=('GET', 'POST'))
def login():
	form = forms.LoginForm()
	if form.validate_on_submit():
		try:
			user = models.User.get(models.User.email == form.email.data)
		except models.DoesNotExist:
			flash("Your email or password doesn't match.", "error")
		else:
			if check_password_hash(user.password, form.password.data):
				login_user(user)
				flash("You've been logged in!", "success")
				return redirect(url_for('index'))
			else:
				flash("Your email or password doesn't match.", "error")
	return render_template('login.html', form = form)

@app.route('/makeListing', methods=('GET', 'POST'))
def makeListing():
	form = forms.NewListingForm()
	if form.validate_on_submit():	
	    address = form.address.data
	    startDate = form.startDate.data
	    endDate = form.endDate.data
	    
	    connection = httplib.HTTPSConnection('api.parse.com', 443)
	    connection.connect()
	    connection.request('POST', '/1/classes/listing', json.dumps({
	        "address": address,
	        "startDate": startDate,
	        "endDate": endDate
	    }), {
	        "X-Parse-Application-Id": parse_app_id,
	        "X-Parse-REST-API-Key": parse_app_key,
	        "Content-Type": "application/json"
	    })
	    result = json.loads(connection.getresponse().read())
	    try:
	        sess_dict = {"id": result['sessionToken'], "objectId": result['objectId']}
	    except KeyError:
	        return jsonify(**result), 400
	    return jsonify(**sess_dict), 201
		#return redirect(url_for('index'))
	return render_template('register.html', form = form)
	
@app.route('/')
def index():
	return 'Hey'	
	
if __name__ == '__main__':
	models.initialize()
	try:
		models.User.create_user(
			username = 'fionarowan',
			email = 'fmr2112@columbia.edu',
			password = 'password',
			admin=True
		)
	except ValueError:
		pass
	app.run(debug=DEBUG, host = HOST, port = PORT)
		