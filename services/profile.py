import twint


def getProfile(username) :
     c = twint.Config()
     c.Store_object = True
     c.Username = username
     
     twint.run.Lookup(c)
     user = twint.output.users_list[-1]
     result = user.__dict__
     result['pfp'] = result['avatar'].replace('_normal', '')
     result.pop('avatar', None)
     return user.__dict__


