import tweepy
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


#INTERVAL = 60 * 60 * 6  # tweet every 6 hours
INTERVAL = 500  # every 15 seconds, for testing
while True:
    api.update_status("Sending my first tweet via Tweepy!")
    time.sleep(INTERVAL)




