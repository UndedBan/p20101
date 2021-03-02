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

user = input("User:")
word_list=[]
persontweets = api.user_timeline(screen_name= user, count=10, include_rts = False)
for tweet in persontweets:
    word_list.append(tweet.text)
words=[]

#Spaei tis lekseis se lista gia na ginei eukola to sort
for tweet in word_list:
    splited = tweet.split()
    words = words + splited

#Sunarthsh gia na taksinomei thn lista me tis lekseis me vash to length
def Taksinomhsh(words):
  words.sort(key=len)
  return words

taksinomhmenes = Taksinomhsh(words)

#Print ta prwta 5 min ths listas
for i in range(5):
  print(taksinomhmenes[i])

#Print ta prwta 5 max ths listas
for j in range((len(words)-5), len(words)):
  print(taksinomhmenes[j])
