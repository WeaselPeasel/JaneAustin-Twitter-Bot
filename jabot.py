### This simple python twitter bot simply reads quotes from a file and posts them to twitter

# import depencies
import tweepy 
import schedule
import random
import time

# enter API key credentials here
consumer_key='XXXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

#authenticating to access the twitter API
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

# set up variables
# number of quotes
length_of_file = 'enter how many quotes are in the file'
index_array = []
quote_file_name = "enter file name here (including file extension)"

for i in range(length_of_file):
	index_array.append(0)	# 0 for unused quote
### get a Jane Austin quote from a file
def post_quote():
	qfile = open(quote_file_name, "r")
	quote_index = random.randint(0,length_of_file-1)
	while index_array[quote_index] == 1:
		quote_index = random.randint(0,length_of_file-1)
	print("QI =", quote_index)
	quote = qfile.readline()
	i = 1
	while i <= quote_index:
	    quote = qfile.readline()
        i += 1
	# post quote to twitter
	api.update_status(quote)
    # mark index as used
	index_array[quote_index] = 1
	print("IA =", index_array)
    # reset if all quotes used up
	reset = True
	for item in index_array:
		if item == 0:
			reset = False
	print("reset =", reset)
	if reset:
		for i in range(len(index_array)):
			index_array[i] = 0
	qfile.close()


### set conditionals for posting quote
schedule.every().monday.at("14:00").do(post_quote)
schedule.every().tuesday.at("14:00").do(post_quote)
schedule.every().wednesday.at("14:00").do(post_quote)
schedule.every().thursday.at("14:00").do(post_quote)
schedule.every().friday.at("14:00").do(post_quote)

while True:
    schedule.run_pending()
    time.sleep(1)
