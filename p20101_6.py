import tweepy

ACCESS_TOKEN =
ACCESS_SECRET =
CONSUMER_KEY =
CONSUMER_SECRET =


def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

api = connect_to_twitter_OAuth()

#project start
xrhsths = input("xrhsths:")
word_list=[]
persontweets = api.xrhsths_timeline(screen_name= xrhsths, count=10, include_rts = False)
for tweet in persontweets:
    word_list.append(tweet.text)

words=[]
for tweet in word_list:
    cracked = tweet.split()
    words = words + cracked

def Sorting(words):
    words.sort(key=len)
    return words

print(Sorting(words))

SYMBOLS = '{}()[].,:;+-*/&|_#!@$%^><\?`=~'

results = []
for element in lekseis:
    temp = ""
    for ch in element:
        if ch not in SYMBOLS:
            temp += ch

    results.append(temp)


for i in range(5):
    print(results[i])

for j in reversed(range(len(results)-5,len(results))):
    print(results[j])
