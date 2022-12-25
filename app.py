from flask import Flask, request, Response
import json
from apis.tweetscrapper import getTweet, getProfile

app = Flask(__name__)

@app.route('/')
def index():
    return "Twitter APi"
    


@app.route('/tweet')
def tweet():
    user = request.args.get('user')
    count = request.args.get('count')
    tweetList = getTweet(user, count)
    jsonArray = parseResponse(tweetList)
    return jsonArray


@app.route('/profile')
def profile():
    user = request.args.get('user')
    profile = getProfile(user)
    jsonArray = parseResponse(profile)
    return jsonArray



def parseResponse(tweetList):
    jsonResult = []
    for tweet in tweetList:
        jsonResult.append(tweet.__dict__)
    return jsonResult


    
app.run(debug=True, host = "localhost", port = 5555)