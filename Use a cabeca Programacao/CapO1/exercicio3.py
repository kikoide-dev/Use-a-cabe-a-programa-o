import time
import tweepy
import urllib.request
from tweepy import OAuthHandler

consumer_key = 
consumer_secret = 

access_token = 
access_token_secret = 


def get_price():
    page = urllib.request.urlopen("https://beans.itcarlow.ie/prices.html")
    text = page.read().decode("utf-8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price +4
    return float(text[start_of_price:end_of_price])

price_now = input("Voce deseja ver o preco agora? (Y/N)")
if price_now =="Y":
   print(get_price())
else:
    price = 99.99
    while price > 4.74:
        time.sleep(900)
    print(get_price())

def send_to_twiiter():
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth)
    text = "texto"
    api.update_status(text)
    
