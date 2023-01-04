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
            return result, 200
        else : 
            raise Exception("invalid tweet id "+ tweetId)
    except Exception as e :
        result = ApiResponse()
        result.code = 404
        result.result = None
        result.error = str(e)
        return result.toJSON(), 400

