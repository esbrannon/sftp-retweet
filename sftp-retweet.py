import tweepy
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


def store_last_id(tweet_id):
    """ Store a tweet id in a file """
    with open("lastid", "w") as fp:
        fp.write(str(tweet_id))

def get_last_id():
    """ Read the last retweeted id from a file """
    with open("lastid", "r") as fp:
        return fp.read()


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    try:
        last_id = get_last_id()
    except FileNotFoundError:
        print("No retweet yet")
        last_id = None

    for tweet in tweepy.Cursor(api.search, q="sftpaa", since_id=last_id).items():
        if tweet.user.name == 'Elliott Brannon':
            store_last_id(tweet.id)
            tweet.retweet()
            print(f'"{tweet.text}" was retweeted'