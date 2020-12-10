import tweepy
import time

from keys import *
import random


print('I am walterbott', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'id.txt'

frases = [
    "No One Promised Life Would Be Perfect",
    "If you look for perfection, you’ll never be content",
    "Success Doesn’t Happen Overnight",
    "Trees that are slow to grow bear the best fruit",
    "There Is a Lesson in Every Struggle",
    "And once the storm is over, you won’t remember how you made it through, how you managed to survive…But one thing is certain. When you come out of the storm, you won’t be the same person who walked in. That’s what this storm’s all about",
    "Strength does not come from winning. Your struggles develop your strengths. When you go through hardships and decide not to surrender, that is strength.",
    "Do not apologize for crying. Without this emotion, we are only robots.",
    "Worry Makes You Suffer Twice",
    "Worry does not empty tomorrow of its sorrow; it empties today of its strength",
    "No One’s Life Is as Picturesque as It Looks",
    "How much time he gains who does not look to see what his neighbor says or does or thinks, but only at what he does himself, to make it just and holy.",
    "Life’s most persistent and urgent question is, ‘What are you doing for others?",
    "There’s Always Something to Be Grateful for",
    "Approach one day at a time and stop trying to tell the future",
    "You’re not alone",
]

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('looking for tweets...', flush=True)

    res = random.choice(frases)
    
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'bad' or "sad" or "help" or "advice" or "problem" in mention.full_text.lower():
            print('found someone asking help...', flush=True)
            print('responding...', flush=True)
            api.update_status('@' + mention.user.screen_name + f" Don´t feel bad. Look at this: {res}", mention.id)
                    

while True:
    reply_to_tweets()
    time.sleep(15)
