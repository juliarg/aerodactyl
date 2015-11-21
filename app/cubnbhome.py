from app import app
from flask import url_for, render_template, g
import os


DATABASE = '/tmp/cubnbhome.db'

#keeps client-side session secure, initializes with random number
SECRET_KEY = os.urandom(24)
USERNAME = 'admin'
PASSWORD = 'default'

@app.route('/')
def home_page():
   #""the home page""
   return render_template('CUBNBhome.html')

@app.route('/account') #/<username>
def profile(username):
    return render_template('account.html')

@app.route('/stay/<username>')
def stay(username):
    return render_template('stay.html')

@app.route('/host/<username>')
def host(username):
    return render_template('host.html')


#tells Flask to behave like its handing a request, even if it's not
#with app.test_request_context():
 #   print url_for('index')
  #  print url_for('profile', username='CU User')
  #  print url_for('stay', username = 'CU User')
  #  print url_for('host', username = 'CU User')


