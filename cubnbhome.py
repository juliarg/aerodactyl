import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \ abort, render_template, flash, os

DATABASE = '/tmp/cubnbhome.db'

#make false for deployment!
DEBUG = True

#listen on all public IPs
app.run(host='0.0.0.0')

#keeps client-side session secure, initializes with random number
SECRET_KEY = os.urandom(24)
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
