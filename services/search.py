import requests
import sys
sys.path.append("..") # Adds higher directory to python modules path
import json
from models.apiresponse import ApiResponse



def searchUserName(userName) :
    try : 
        headers = {'x-csrf-token': '405122eb7d1405d6ab3ccd2fca7c8d32510f669e79da4bb7e47c7767dda7d43ebe46f8c155318974583aa351c51e308b10da0d02e912010bb2c4e68195e96593dd0a49292d4716d77b16a8ec9fd1f8d3', 
            'authorization' : 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'cookie' : 'guest_id_marketing=v1%3A166722245099469341; guest_id_ads=v1%3A166722245099469341; des_opt_in=Y; _gcl_au=1.1.1530671685.1669068812; kdt=mHqUMhnsFUkdtPzJHY8iuFJ8wYzo91XdLJTQLqYE; tweetdeck_version=legacy; _ga_J2XYV9CGE1=GS1.1.1673175435.1.0.1673175435.0.0.0; at_check=true; lang=en; _ga_34PHSZMC42=GS1.1.1673439356.12.0.1673439393.0.0.0; _ga=GA1.2.1450780084.1667286478; dnt=1; personalization_id="v1_x6XjtO1wItnTvwa0750KZQ=="; guest_id=v1%3A167343943603176675; mbox=PC#da8aa9a919f14f929040d0e8bd0a60be.31_0#1736684247|session#b75ca92d523e48d9b111f3cbb002e42b#1673441307; external_referer=padhuUp37zixoA2Yz6IlsoQTSjz5FgRcKMoWWYN3PEQ%3D|0|8e8t2xd8A2w%3D; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCBuRw6CFAToMY3NyZl9p%250AZCIlYzEzZWJhMjkzZDdlZTIyZjhmNjQ4MGY4MWVkZTczNjA6B2lkIiU1NDAw%250AYWFmYjAyNDllYzgzZDBmYTI0ZGFiMjIzMDViYQ%253D%253D--9fb80d34435243601b916b1b3157d68a3b29d92e; gt=1614305468612251648; _gid=GA1.2.1675579042.1673715391; auth_token=08dfbbc5b3f546f66cfec703868efa723e1e3c73; ct0=405122eb7d1405d6ab3ccd2fca7c8d32510f669e79da4bb7e47c7767dda7d43ebe46f8c155318974583aa351c51e308b10da0d02e912010bb2c4e68195e96593dd0a49292d4716d77b16a8ec9fd1f8d3; twid=u%3D584613533; att=1-qLLnptUhzjxiPXDTFmGxH3yuwjE9djfKRCxGhZTR'
        }
        r = requests.get('https://api.twitter.com/1.1/users/search.json?q=' + userName ,headers=headers)
        result = {}
        jsonResult = []


        for x in r.json():
            jsonObject = {}
            jsonObject['id'] = x["id"]
            jsonObject['username'] = x['screen_name']
            jsonObject['pfp'] = x['profile_image_url_https'].replace('_normal', '')
            jsonObject['name'] = x['name']
            jsonObject['bio'] = x['description']
            jsonObject['following'] = x['friends_count']
            jsonObject['followers'] = x['followers_count']
            jsonObject['is_verified'] = x['verified']

            jsonResult.append(jsonObject)

        result = ApiResponse()
        result.code = 200
        result.result = jsonResult
        result.error = None
        
        return result.toJSON(), 200
    except Exception as e :
        result = ApiResponse()
        result.code = 404
        result.result = None
        result.error = e
        return result.toJSON(), 400

