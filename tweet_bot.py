'''
Libraries used are Tweepy,urlparse ,TwitterAPI and OAuth1
'''


import tweepy
import requests
from TwitterAPI import TwitterAPI
import time
from requests_oauthlib import OAuth1
from urlparse import parse_qs
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


auth = tweepy.OAuthHandler(ck,cs)
auth.set_access_token(tk,ts)
temp2 = str()
tweeter = list()
receiver = list()
api = tweepy.API(auth)
hashtweet = tweepy.Cursor(api.search,q='#HappyBirthday').items(50)
for tweet in hashtweet:
	x = tweet.user.id_str
	y = '@'+api.get_user(x).screen_name
	tweeter.append(y)
	temp = tweet.text
	words = temp.split()
	for word in words:
		if word.startswith('@') and len(word)>2:
			temp2 = word
			receiver.append(temp2)


#requesting api 


api = TwitterAPI(ck, cs, tk, ts)
for user in receiver:
	line = 'Happy Birthday ' +user+ ' From Wishfie!'
	r = api.request('statuses/update', {'status' : line}) #line is the tweet here.
	print line
	print '$'
	print r.status_code
time.sleep(60)