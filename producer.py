from kafka import KafkaProducer
from tweepy import OAuthHandler
from tweepy import AppAuthHandler
from tweepy import API
from tweepy import Cursor
from tweepy import TweepError
from tweepy.streaming import StreamListener
from tweepy import Stream
import time

consumer_key = "dPmHS7bNm5a5osJcn0NPgFV34"
consumer_secret = "0yuR2hRUcv2tLV6rgDWtZzEnVXUMKj6OXgrDUMQ9zc2zOYdlYk"
access_token = "1342058413107384321-WDmYva8hgjnLqNGQanT3XAyQFctDkS"
access_token_secret = "q0wAXiogkkG8KgWIasGKmdgSFaUDSzON8tpHKGfK2NI4E"


producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic_name = "twitterdata"

class TwitterAuth():
    def authenticateTwitterApp(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth

class ListenerTS(StreamListener):
    def on_status(self, status):
        print("on status")
        print(status.text)

    def on_data(self, raw_data):
        print("on data")
        producer.send(topic_name, str.encode(raw_data))
        print(str.encode(raw_data))
        return True

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            #returning False in on_error disconnects the stream
            print("error")
            return False

class TwitterStreamer():
    def __init__(self):
        self.twitterAuth = TwitterAuth()
    
    def stream_tweets(self):
        while True:
            listener = ListenerTS() 
            auth = self.twitterAuth.authenticateTwitterApp()
            stream = Stream(auth, listener)
            # api = API(auth)
            # for tweet in Cursor(api.search, q='tweepy').items(10):
            #     print(tweet.text)
            # stream.filter(track=["Apple"], stall_warnings=True, languages=["fr"])
            stream.filter(track=["python"], is_async=True)
            # print("*")
            time.sleep(18)

def getAccessTokenAndSecret():
    auth = OAuthHandler(consumer_key, consumer_secret)
    try:
        redirect_url = auth.get_authorization_url()
        print(redirect_url)
    except TweepError:
        print('Error! Failed to get request token.')
    verifier = input('Verifier:')

    try:
        auth.get_access_token(verifier)
    except TweepError:
        print('Error! Failed to get access token.') 

    print("Access token :", auth.access_token)
    print("Access token secret :", auth.access_token_secret)

if __name__ == "__main__":
    TS = TwitterStreamer()
    TS.stream_tweets()