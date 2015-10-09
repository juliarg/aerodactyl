from flask import Flask, jsonify, render_template 
import requests

app = Flask(__name__)

@app.route("/")

def hello(): 
	return render_template("hello.html")
	
@app.route("/name")
def name(): 
	return "Your Name" 
	
@app.route("/website")
def website(): 
	return "https://twitter.com/"
	
@app.route("/search/<search_query>")
def search(search_query):
	url = "https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript" + search_query
  	response_dict = requests.get(url).json()
  	#response_dict = parse_response(response_dict)
  	return jsonify(response_dict)

def parse_response(response_dict):
	clean_response = response_dict[items][name][owner][login][avatar_url][html_url][html_url][description] 
	return clean_response
	
@app.route("/add/<x>/<y>")
def add(x, y):
	return str(int(x) + int(y))

@app.errorhandler(404)
def page_not_found(error):
    return "Oh, no! Where is this page?", 404
	
if __name__ == "__main__":
	app.run(host="0.0.0.0")
	
