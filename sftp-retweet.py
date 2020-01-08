import tweepy

CONSUMER_KEY = 'SVPmqMF4QgOr6zDPCw2vN6Rld'
CONSUMER_SECRET = '8mg9pmt0RWrbyKIdQS3MwymJM23fQRne3j4UmKIcshepeb7yiY'
ACCESS_KEY = '3192182461-61si4xpOxfYoDHuABRhJT2Nkz3b0WRdwGaXvAdl'
ACCESS_SECRET = 'IgAbEsuUczuyCqwUqRLnXy9JhNhH6tqSs5b21qgfaWmLi'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("Sending my first tweet via Tweepy!")
