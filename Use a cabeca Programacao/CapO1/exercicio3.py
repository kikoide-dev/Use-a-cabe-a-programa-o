import time
import tweepy
import urllib.request
from tweepy import OAuthHandler

consumer_key = 'OV4o3wgmlZjdRC3O5Mf9hcVpZ'
consumer_secret = 'YgnJQDTTZ8ni5NyZa7Za33CuKVvRvuiqfKT08rReLWdCeDcqZk'

access_token = '1697398803416965120-RsFW2NGhOWO9I7lhl1Jt5my7FX8uGb'
access_token_secret = 'fHkdIctW1Xq12i44IhftDa3AMANl2zqBxS3Wr9aF6q4d0'


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
    