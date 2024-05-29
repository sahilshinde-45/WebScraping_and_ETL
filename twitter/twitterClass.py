from typing import Collection
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import fileClass
import twitterAccess
from tweepy.api import API
from tweepy import Cursor
import numpy as np
import pandas as pd 
import fileClass
import string


class Twitterclient():
    def __init__(self,twitter_user=None):
        self.auth = twitterAuthenticator().authenticate_twitter_api()
        self.twitter_client = API(self.auth) 
        self.twitter_user = twitter_user
    
    def get_client_api(self):
        return self.twitter_client

    def get_user_tweets(self,num_tweets):
        tweets =[]
        for tweet in self.Cursor(self.twitter_client.user_timeline,id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

class twitterAuthenticator():
    
    def authenticate_twitter_api(self):
        auth = OAuthHandler(twitterAccess.API_KEY,twitterAccess.API_KEY_SECRET)
        auth.set_access_token(twitterAccess.ACCESS_TOKEN,twitterAccess.ACCESS_TOKEN_SECRET)
        return auth

class fetchTweet():

    def __init__(self):
        self.twitter_authenticator = twitterAuthenticator()

    def stream_tweets(self,fetched_tweets_filename,track_list):
        listener = StdOutListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_api() 
        stream = Stream(auth,listener)
        stream.filter(track=track_list)

class StdOutListener(StreamListener):

    # printing out the data from twitter
    
    def __init__(self, fetched_tweet_filename):
        self.fetched_tweet_filename = fetched_tweet_filename
    
    
    def on_data (self,data):
        try:
            print(data)
            with open (self.fetched_tweet_filename,'a')as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("ERROR ON_DATA : " ,str(e))
            return True

    def on_error (self,status):
        if status == 420:
            #returning false on_data in case rate limit occurs. 
            return False
        print(status)

class tweetAnalyzer():
    #basically going to fetch the important part of the tweet
    
    def clean_csv_twitterFile(self):
        file_obj = fileClass.files('twitter1.csv',',')

        data = file_obj.showfile()
        for i in data:
    
            i[1]=i[1].encode('latin-1','replace').decode('latin-1')
            i[1]=str(i[1]).translate(str(i[1]).maketrans('','',string.punctuation))
    
            #print(i)
            #print(data)
        parse=file_obj.writeTableToFile('twitter_final.csv')
        for item in data:
            #print(item)
            parse.writerow(item)

        file_obj.closefile()
    

    
    def tweet_to_data_frame(self,tweets):
        self.tweets = tweets
        df = pd.DataFrame(data= [tweet.text for tweet in self.tweets],columns=['tweets'])
        
        df['id']= np.array([tweet.id for tweet in self.tweets])
        df['tweet_len']= np.array([len(tweet.text) for tweet in self.tweets])
        df['date']= np.array([tweet.created_at for tweet in self.tweets])
        df['source']= np.array([tweet.source for tweet in self.tweets])
        df['likes']= np.array([tweet.favorite_count for tweet in self.tweets])
        df['retweets']= np.array([tweet.retweet_count for tweet in self.tweets])
        
        return df

