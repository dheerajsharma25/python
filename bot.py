import tweepy
from tweepy.streaming import StreamListener
from pprint import pprint
import sys
import time
import json
import pandas as pd
import matplotlib.pyplot as plt
while True:

    print("1.Retrive tweets")
    print("2.Count the followers")                  #menu_list
    print("3.Determine the status")
    print("4.Location language and Time Zone")
    print("5.compare tweets")
    print("6.Sentiment the Tweets")
    print("7.Text a message")
    print("8.To ploat the Graph")
    print("9.Exit")
    choice=int(input("Enter your choice: "))
    consumer_key = ""                               
    consumer_secret = ''                     
    access_token = ''                          
    access_token_secret = ''                     
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)
    def retrive():                                                      #for retrive the tweets
        m=str(input("enter any HASH tag for search:"))
        tweets=api.search(m,lang='english',count="50",tweet_mode='extended')
        print(tweets)
        for tweet in tweets:
            print("---------------------------------")
            print(tweet.full_text)                                           #tweets are printed
            print("---------------------------------")
    def followers():
        user_id=input("enter any id to Count the followers:")               #for counting the followers
        user=api.get_user(user_id)
        print("user_id : ",user.screen_name)
        print("user_name:",user.name)
        print("user_following : ",user.friends_count)
        print("followers :",user.followers_count)
        return
    def status():                                                   #to upload the status
        status=input("enter any Status: ")
        user_id = input("enter any id to upload the status:")
        api.update_status(status,user_id)
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


    def get_tweets(username):                                #sentimental analysis
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        tweets = api.user_timeline(screen_name=username, count=20)
        tmp = []
        tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created
        for j in tweets_for_csv:
            tmp.append(j)                   # store the tweets in tmp list        
        var1 = 0
        var2 = 0
        var3 = 0

        print(tmp)
        from paralleldots import set_api_key, get_api_key, sentiment
        set_api_key("6dm9k0RomplpimtZETEkwp6JzMTrPSDhhMIiGPGmu68")
        get_api_key()
        for t in tmp:
            a = sentiment(t)
            print(a)
            if a['sentiment'] == 'positive':            #checking positive tweets
                var1 += 1
            if a['sentiment'] == 'negative':            #checking negative tweets
                var2 += 1
            if a['sentiment'] == 'neutral':             #checking neutral tweets
                var3 += 1
        if (var1 > var2) and (var1 > var3):         #checking the person is positive or not
            print("positive")
        if (var2 > var3) and (var2 > var1):         #checking the person is negative or not
            print("negative")
        if (var3 > var2) and (var3 > var1):         #checking the person is neutrl or not
            print("neutral")
    def comp():                                     #for comare the which twitter user is mostly active on twitter
        user_id = input("enter 1st id to Compare:")
        user = api.get_user(user_id)
        a1= user.followers_count
        user_id1 = input("enter 2nd id to Compare:")
        user1 = api.get_user(user_id1)
        a2 = user1.followers_count
        if a1>a2:                           # comarision
            print("{} is the best user of twitter".format(user.name))
        else:
            print("{} is the best user of twitter".format(user1.name))
    def Ploat_graph():                                          #to ploat the graph of python,javascript,ruby according to their useses in twitter
        class StdOutListener(StreamListener):

            def on_data(self, data):
                print(data)
                return True

            def on_error(self, status):
                print(status)

        l = StdOutListener()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = tweepy.Stream(auth,l)
        stream.filter(track=['python', 'javascript', 'ruby'])

        tweets_data_path = 'D:/twitter_data.txt'            #storing the data json file to text file
        tweets_data = []
        tweets_file = open(tweets_data_path, "r")
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except:
                continue
        print(len(tweets_data))
        tweets = pd.DataFrame()
        tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
        tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
        tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
        tweets_by_lang = tweets['lang'].value_counts()
        fig, ax = plt.subplots()                            # to ploat the graph
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=10)
        ax.set_xlabel('Languages', fontsize=15)
        ax.set_ylabel('Number of tweets', fontsize=15)
        ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
        tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

        tweets_by_country = tweets['country'].value_counts()

        fig, ax = plt.subplots()                        # to ploat the sub graph of language
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=10)
        ax.set_xlabel('Countries', fontsize=15)
        ax.set_ylabel('Number of tweets', fontsize=15)
        ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
        tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')


    if choice==1:               #checking user choice
        retrive()           #calling the function
    if choice==2:               #checking user choice
        followers()         #calling the function
    if choice==3:               #checking user choice
        status()             #calling the function
    if choice==4:               #checking user choice
        loc()                 #calling the function
    if choice==5:               #checking user choice
        comp()                 #calling the function
    if choice==6:                #checking user choice
        username = input("enter any user id:")
        get_tweets(username)     #calling the function
    if choice==7:               #checking user choice
        direct_msg()          #calling the function
    if choice==8:               #checking user choice
        Ploat_graph()           #calling the function
    if choice==9:               #checking user choice
        exit()