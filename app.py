from flask import Flask, request, Response, send_from_directory
from services.tweetscrapper import getTweet, getBulkTweets
from models.apiresponse import ApiResponse
from services.search import searchUserName
from logging import FileHandler,WARNING


app = Flask(__name__, static_url_path='/static')

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

@app.route('/', methods=['GET'])
def index():
    return send_from_directory("static", 'index.html')


@app.route('/search/<username>', methods=['GET'])
def search(username):
    return searchUserName(username)
    
@app.route('/tweet/<username>', methods=['GET'])
@app.route('/tweet/<username>/<count>', methods=['GET'])
def tweet(username, count = 20):
    start = request.args.get('start')
    end = request.args.get('end')

    result = getTweet(username, count, start, end)
    return result 


@app.route('/tweets/', methods = ['POST'])
@app.route('/tweets/<count>', methods = ['POST'])
def multiple(count = 20):
    try : 
        usersArray = request.json
        if(usersArray is not None and len(usersArray) > 0):
            start = request.args.get('start')
            end = request.args.get('end')
            resultTweets = getBulkTweets(usersArray, count, start, end)
            return resultTweets
        else :
             apiResponse = ApiResponse()
             apiResponse.code = 404
             apiResponse.result = []
             apiResponse.error = "User list is empty"
             return apiResponse.toJSON(), 404

    except Exception as e :
        apiResponse = ApiResponse()
        apiResponse.code = 404
        apiResponse.result = []
        apiResponse.error = e
        return apiResponse.toJSON(), 404


if __name__ == "__main__":
    app.run(debug = True)