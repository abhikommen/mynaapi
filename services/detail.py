import requests
import sys
sys.path.append("..") # Adds higher directory to python modules path
import json
from models.apiresponse import ApiResponse


def getDetail(tweetId) :
    try : 
        body = {"tweetId":tweetId}
        r = requests.post('https://pika.style/api/templates/web-tweet-image', json = body)
        jsonResponse = r.json()
        # return jsonResponse
        if "tweet" not in jsonResponse:
            result = {}
            result["author_id"] = jsonResponse["data"]["author_id"]
            result["created_at"] = jsonResponse["data"]["created_at"]
            result["like_count"] = jsonResponse["data"]["public_metrics"]["like_count"]
            result["quote_count"] = jsonResponse["data"]["public_metrics"]["quote_count"]
            result["reply_count"] = jsonResponse["data"]["public_metrics"]["reply_count"]
            result["retweet_count"] = jsonResponse["data"]["public_metrics"]["retweet_count"]
            result["text"] = jsonResponse["data"]["text"]
            try :
                urls = []
                for item in jsonResponse["includes"]["media"] :
                    url = {}
                    if(item['type'] == "photo"):
                        url["type"] = "photo"
                        url["url"] = item['url']
                    elif (item['type'] == "video"):
                        url["type"] = "video"
                        url['thumbnail'] = item['preview_image_url']
                        url['url'] = item['variants'][0]['url']
                    elif (item['type'] == "animated_gif"):
                        url["type"] = "gif"
                        url['thumbnail'] = item['preview_image_url']
                        url['url'] = item['variants'][0]['url']

                    urls.append(url)
                result["media"] = urls

            except BaseException as e : 
                print(repr(e))

            currentUser = jsonResponse["includes"]["users"][0]    

            user = {}
            user['id'] = currentUser["id"]
            user['user_name'] = currentUser['username']
            user['pfp'] = currentUser['profile_image_url'].replace('_normal', '')
            user['name'] = currentUser['name']
            user['description'] = currentUser['description']
            user['following'] = currentUser['public_metrics']['following_count']
            user['followers'] = currentUser['public_metrics']['followers_count']
            user['verified'] = currentUser['verified']

            result['user'] = user

            apiResponse = {}
            apiResponse["code"] = 200
            apiResponse["result"] = result
            apiResponse["error"] = None
            return apiResponse, 200
        else : 
            raise Exception("invalid tweet id "+ tweetId)
    except Exception as e :
        result = ApiResponse()
        result.code = 404
        result.result = None
        result.error = str(e)
        return result.toJSON(), 400

