from kafka import KafkaProducer
from tweepy import OAuthHandler
from tweepy import AppAuthHandler
from tweepy import API
from tweepy import Cursor
from tweepy import TweepError
from tweepy.streaming import StreamListener
from tweepy import Stream
import time

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic_name = "twitterdata"

class TwitterAuth():
    def authenticateTwitterApp(self):
        """Authentification avec les token auprès de l'api twitter"""
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth

class ListenerTS(StreamListener):
    """Le listener"""
    def on_status(self, status):
        print(status.text)

    def on_data(self, raw_data):
        """Reception de données"""
        producer.send(topic_name, str.encode(raw_data))
        return True

    def on_error(self, status_code):
        """Erreur, 420 : on appelle trop"""
        print(status_code)
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

class TwitterStreamer():
    def __init__(self):
        self.twitterAuth = TwitterAuth()
    
    def stream_tweets(self):
        while True:
            listener = ListenerTS() # on crée le listener
            auth = self.twitterAuth.authenticateTwitterApp() # on s'authentifie auprès de api twitter
            stream = Stream(auth, listener) # on débute un stream
            stream.filter(track=["python"], is_async=True) # on filtre par mot clef et en asynchrone
            time.sleep(18) # 50 appels / 15 minutes max

def getAccessTokenAndSecret():
    """Récupérer les token de connexion
    Ils restent valides pour une période infinie, pas besoin de rappeler la fonction"""
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