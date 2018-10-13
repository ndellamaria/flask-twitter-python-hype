import os
import time
import flask
import tweepy
from twitter import *
from flask import Flask, request, render_template

OAUTH_TOKEN="2464717370-ztIheNqKFIr9ll1ZG3OEa1SxRPTGY8k1XL3Ukj0"
OAUTH_SECRET="doEQPqBTLo22FrakNfY2q3jdLJyary6TFcLT8sv8AJes7"
CONSUMER_KEY="0J1e4CLZOLJTG1fVQaQya4fH1"
CONSUMER_SECRET="SUZK3xOyW4DJzY0rqr8pr2PQuVjEjEPgUNd73fMYd5eXSg4sY9"

app = Flask(__name__)

twitter = Twitter (
	auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
) 

@app.route('/')

def main():

	# fetch 3 tweets from my account
	mytweets = twitter.statuses.user_timeline(count=10, screen_name="CUhackit")

	# app.logger.debug(itpTweets)

	templateData = {
		'title' : 'My last three tweets',
		'mytweets' : mytweets,
	}

	return flask.render_template("index.html", **templateData)



# @app.route('/templates/')
# def index():
# 	return flask.render_template("index.html", **templateData)

if __name__ == '__main__':
	# auth = tweepy.OAuthHandler()

	app.debug=True
	app.run()


