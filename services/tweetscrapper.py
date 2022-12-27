import twint
from datetime import datetime
from multiprocessing.pool import ThreadPool


def request(user, count, start, end):
    tweets = []
    c = twint.Config()
    c.Username = user
    c.Limit = count
    c.Store_object = True
    c.User_full = True

    if start is not None and end is not None and start.isnumeric() and end.isnumeric():
        print(start)
        since = datetime.fromtimestamp(int(start))
        until = datetime.fromtimestamp(int(end))
        c.Since = str(since) 
        c.Until = str(until)

    c.Store_object_tweets_list = tweets
    twint.run.Search(c)
    return tweets

def getTweet(user, count, start, end):
    
    try:
        resultTweets = request(user, count, start, end)
        return parseResponse(resultTweets, count)

    except ValueError as ve:
        result = {}
        result['result'] = None
        result['code'] = 404
        result['error'] = str(ve)
        return result, 404


def parseResponse(tweetList, limit):
    result = {}
    jsonResult = []
    for tweet in tweetList:
        jsonResult.append(tweet.__dict__)
    
    result['result'] = jsonResult
    result['code'] = 200
    result['error'] = None
    return result, 200



def getBulkTweets(users, count, start, end):
    result = []
    args = []
    for u in users:
      args.append((u, count, start, end))

    pool = ThreadPool(len(users)) 
    for res in pool.starmap(request, args, 1):
        result.extend(res)
    
    return parseResponse(result, 10)
    