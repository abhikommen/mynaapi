import requests
import json


def searchUserName(userName, size) : 
    headers = {'x-csrf-token': 'b3480dfa0eb9829464eeaf514dccbd01cdf5d2877f963410ff90c7e92d781862243214bc694ff6e07029b6be4278d95b6d1221d2cec9badb176c4e5ac5c39058e288a7d0780599b7f13d5bac0df0586c', 
        'authorization' : 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'cookie' : 'personalization_id="v1_2gTiSoEcNtZfrBMeJ8pTDQ=="; guest_id_marketing=v1%3A166722245099469341; guest_id_ads=v1%3A166722245099469341; guest_id=v1%3A166722245099469341; des_opt_in=Y; _gcl_au=1.1.1530671685.1669068812; g_state={"i_p":1673448523599,"i_l":4}; at_check=true; _gid=GA1.2.1911685362.1671202755; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoHaWQiJTY0NDhkMDRjZGM0ZThhOGFlMmI1ZTEx%250ANTg1MWFhOTVkOg9jcmVhdGVkX2F0bCsIMtxyG4UBOgxjc3JmX2lkIiUxY2Fj%250AMWYyMGVkYjNmNzdmMWI1YmNhMGJkOWNkMGE2Yg%253D%253D--04bdcd906c3b68b8edaf698d9576f302e2ed390d; kdt=mHqUMhnsFUkdtPzJHY8iuFJ8wYzo91XdLJTQLqYE; auth_token=fda7ff69427d471e23f98b9568f2500ce85ac205; ct0=b3480dfa0eb9829464eeaf514dccbd01cdf5d2877f963410ff90c7e92d781862243214bc694ff6e07029b6be4278d95b6d1221d2cec9badb176c4e5ac5c39058e288a7d0780599b7f13d5bac0df0586c; twid=u%3D584613533; att=1-xjLCjLbP7N71hOK21rZfcN27egdinb7E7rrJpDGn; tweetdeck_version=legacy; external_referer=padhuUp37zj9xuUOXCNFvKjMgOBpP9isUogtir%2FOEmtI%2F1%2FfDC2%2F2inrCVui3enUvUPzgRzQC7A%3D|0|8e8t2xd8A2w%3D; mbox=PC#da8aa9a919f14f929040d0e8bd0a60be.31_0#1734458015|session#8db3eacfd5fd41daa380c29046382fa3#1671215075; _ga_34PHSZMC42=GS1.1.1671213219.5.1.1671213415.0.0.0; _ga=GA1.2.1450780084.1667286478'
    }
    r = requests.get('https://api.twitter.com/1.1/users/search.json?q=' + userName ,headers=headers)
    

    result = {}
    jsonResult = []

    for x in r.json():
        jsonObject = {}
        jsonObject['id'] = x["id"]
        jsonObject['user_name'] = x['screen_name']
        jsonObject['pfp'] = x['profile_image_url']
        jsonObject['name'] = x['name']
        jsonObject['description'] = x['description']
        jsonObject['following'] = x['friends_count']
        jsonObject['follwers'] = x['followers_count']

        jsonResult.append(jsonObject)

    result['size'] = len(r.json())
    result['result'] = jsonResult
    
    return result

