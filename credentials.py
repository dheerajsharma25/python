import tweepy
from tweepy import OAuthHandler
from textblob import *

import time
import json

consumer_key = 	'fgkjhbghkjshdfbgkjgbkjbfv'
consumer_secret = 'dfhgsdfvdjkhvfdskjvbgfdkjbhvgfbhnlhgfdjhv'

Access_token = 	',kjsjdhghgfshgeriugsighbsnjbvndfbv'
Access_secret = 'cjhsdfhvgsdivhdshjgvvbvkj'

auth =tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(Access_token,Access_secret)
api = tweepy.API(auth)




# user = api.me()
# print("Hey your username is :",user.name)

# for status in tweepy.Cursor(api.home_timeline).items(10):
    #Process a single status
    # print(status.text)
	
   
# def limit_handled(cursor):
	# while True:
		# try:
			# yield cursor.next()
		# except tweepy.RateLimitError:
			# time.sleep()
# for follower in limit_handled(tweepy.Cursor(api.followers).items()):
	# if follower.friends_count < 300:
		# print(follower.screen_name)
		
# public_tweet=api.search('smile')

# for tweet in public_tweet:
	# print(tweet.text)
	# analysis = TextBlob(tweet.text)
	# print(analysis.sentiment)
	
def loc():                                                       # for location ,time_zone and language
        user_id = input("enter any id to see location:")
        user = api.get_user(user_id)
        print("location :",user.location)
        print("Time Zone:",user.time_zone)
        print("language: ",user.lang)
    def direct_msg():                                       #to send the direct msg
        user_id= input("enter any id to send msg:")
        msg=input("enter any msg:")
        api.send_direct_message(user=user_id,text=msg)
	
	
	
	
	
	