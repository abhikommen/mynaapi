import twint


def getTweet(user, count):
    tweets = []
    c = twint.Config()
    c.Username = user
    c.Limit = count
    c.Store_object = True
    c.Store_object_tweets_list = tweets
    twint.run.Search(c)
    return tweets

def getProfile(user):
    profile = []
    c = twint.Config()
    c.Username = user
    c.Store_object = True
    c.Store_object_users_list = profile
    twint.run.Lookup(c)
    return profile
