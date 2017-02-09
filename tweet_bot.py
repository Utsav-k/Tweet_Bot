'''
Libraries used are Tweepy,urlparse ,TwitterAPI and OAuth1
'''


import tweepy
import requests
from TwitterAPI import TwitterAPI
import time

'''
account datails collected from twitter app service
for getting these details go to : 'https://apps.twitter.com/'
ck = Consumer Key(API Key)
cs = Consumer Secret(API Secret)
tk = Access Token
ts = Access Token Service
'''
# all the four parameters are string data type

#Searching usernames with Hashtag parameter


auth = tweepy.OAuthHandler(ck,cs)   #creating auth object
auth.set_access_token(tk,ts)
temp2 = str()
tweeter = list()
receiver = list()
api = tweepy.API(auth)
hashtweet = tweepy.Cursor(api.search,q='#HappyBirthday').items(50)   # q = item to be searched
for tweet in hashtweet:
	x = tweet.user.id_str
	y = '@'+api.get_user(x).screen_name
	tweeter.append(y)
	temp = tweet.text
	words = temp.split()
	for word in words:
		if word.startswith('@') and len(word)>2:   #parsing tagged person's user name
			temp2 = word
			receiver.append(temp2)


#requesting api 


api = TwitterAPI(ck, cs, tk, ts)   #creating API object
for user in receiver:
	line = 'Happy Birthday ' + user    # what to tweet?  
	r = api.request('statuses/update', {'status' : line}) #line is the tweet here.
	print line
	print '$'
	print r.status_code   #if out put is 200 , it means you've tweeted successfully.
time.sleep(60)
