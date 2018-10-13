import os
import time
import flask
# from twitter import *
from flask import Flask, request, render_template

app = Flask(__name__)

# twitter = Twitter (
# 		auth=OAuth(os.environ.get('OAUTH_TOKEN'), os.environ.get('OAUTH_SECRET'), os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
# 	) 

@app.route('/')
def index():
	return flask.render_template("index.html")

if __name__ == '__main__':
	app.debug=True
	app.run()


