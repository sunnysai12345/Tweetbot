from twitter import *
access_token = ''
access_token_secret = ''
consumer_key =''
consumer_secret =''
t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
searchfor=raw_input('enter string:')
x=t.search.tweets(q=searchfor)
for i in range(15):
    s=x['statuses'][i]['text']
    t.statuses.update(status=s)
    
