import tweepy
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

def main():
    search_term = ('sftpaa')
    number_of_tweets = 5

    for tweet in tweepy.Cursor(api.search, search_term).items(number_of_tweets):
        try:
            print('\nFound tweet by @' + tweet.user.screen_name)
            tweet.retweet()
            print("Yay! Tweet was retweeted :)")

            # sleep is measured in seconds
            sleep(10)

        except tweepy.TweepError as error:
            print('wtf, why isn\'t it working?' + error.reason)

        except StopIteration:
            break


main()