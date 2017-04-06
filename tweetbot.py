from twitter import *
def tweetbot():
    #Fill the details below
    access_token = ''
    access_token_secret = ''
    consumer_key =''
    consumer_secret =''
    t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
    #Enter search string
    searchfor=raw_input('enter string:')
    x=t.search.tweets(q=searchfor)
    #Set range for how many tweets u want to send
    for i in range(15):
        s=x['statuses'][i]['text']
        t.statuses.update(status=s)
if __name__== '__main__':
    tweetbot()
    


    
