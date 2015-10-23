from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index(): pass

@app.route('/account/<username>')
def profile(username): pass

@app.route('/stay/<username>')
def stay(username): pass

@app.route('/host/<username>')
def host(username): pass


#tells Flask to behave like its handing a request, even if it's not
with app.test_request_context():
    print url_for('index')
    print url_for('profile', username='CU User')
    print url_for('stay', username = 'CU User')
    print url_for('host', username = 'CU User')

