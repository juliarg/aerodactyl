from app import app
import os

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'


app.run(host=HOST, debug=DEBUG, port=PORT)