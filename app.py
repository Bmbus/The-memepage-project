import tweepy
import praw
import urllib.request
import os
from config import *

# Init tweepy (twitter)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Init praw (reddit)
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username
)

def get_meme():
    """GET MEME FROM REDDIT"""

    subreddit = reddit.subreddit("memes")
    meme = subreddit.random()
    img_name = meme.url.split(".it/")[1]
    while True:
        if img_name.endswith(".gif"):
            continue
        urllib.request.urlretrieve(meme.url, img_name)
        break
    
    return img_name

def delete_img(file):
    """DELETE THE DOWNLOADED MEME"""

    return os.remove(file)

def uplaod_meme():
    """UPLAOD MEME TO TWITTER"""

    meme = get_meme()
    media = api.media_upload(meme)

    status = api.update_status(status="#meme", media_ids=[media.media_id])

    delete_img(meme)

    return status

if __name__ == '__main__':
    uplaod_meme()