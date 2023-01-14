from tweety.bot import Twitter

app = Twitter()

all_searches = app.search("Pakistan")
print(all_searches)