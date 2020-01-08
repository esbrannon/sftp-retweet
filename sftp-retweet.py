import tweepy
from os import environ
from apscheduler.schedulers.blocking import BlockingScheduler

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=10)
def timed_job():
    api.update_status("Sending my first tweet via Tweepy!")

sched.start()



