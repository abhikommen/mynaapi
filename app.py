from flask import Flask
from flask import request

import twint
import json 

from apis.search import searchUserName

app = Flask(__name__)

tweets = []

@app.route('/home')
def index():
    hello()
    return json.dumps(tweets[0].__dict__)


@app.route('/search')
def search():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')
    count = request.args.get('count')
    print(count)
    jsonResult = searchUserName(user, count)
    return jsonResult


def hello():
    c = twint.Config()
    c.Username = "elon musk"
    c.Limit = 10
    c.Store_object = Truep
    c.Store_object_tweets_list = tweets
    twint.run.Search(c)



app.run(debug=True, host='0.0.0.0', port=81)