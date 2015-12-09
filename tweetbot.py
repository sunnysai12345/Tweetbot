from twitter import *
def tweetbot():
    access_token = '396545890-p9hJW2yKDUyRIoSAllg7MKRsLiGoG79Ja9X4WqxI'
    access_token_secret = 'CW4eJko1xogxWWZ6DQp2X1Q554QnJnz8ZBTJUHL93SVdq'
    consumer_key ='KDI8fveXLwn5l7r1Vww11QIzd'
    consumer_secret ='NmtTtWQhzQuu2TGq8vGDaM6EGz71JtW3ncWtt44QfA7rfU97fE'
    t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
    searchfor=raw_input('enter string:')
    x=t.search.tweets(q=searchfor)
    for i in range(15):
        s=x['statuses'][i]['text']
        t.statuses.update(status=s)
if __name__== '__main__':
    tweetbot()
    


    
