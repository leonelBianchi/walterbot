import tweepy
import time

from keys import *
import random
import datetime


print('I am walterbott', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'id.txt'


frases = [
    "You clearly don’t know who you’re talking to, so let me clue you in.", 
    "A guy opens his door and gets shot, and you think that of me? No! I am the one who knocks!",
    "Right now, what I need, is for you to climb down out of my ass. Can you do that?",
    "Smoking marijuana, eating Cheetos, and masturbating do not constitute plans in my book.",
    "Fuk you, and your eyebrows.",
    "If you don’t know who I am, then maybe your best course would be to tread lightly.",
    "Is this just a genetic thing with you? Is it congenital? Did your, did your mother drop you on your head when you were a baby?",
    "I have spent my whole life scared, frightened of things that could happen, might happen, might not happen, 50 years I spent like that.", 
    "Ever since my diagnosis, I sleep just fine. What I came to realize is that fear, that’s the worst of it. That’s the real enemy",
    "So, get up, get out in the real world and you kick that bastard as hard you can right in the teeth.",
    "I did it for me. I liked it. I was good at it. And, I was really…I was alive.",
    "Jesse, you asked me if I was in the meth business, or the money business… Neither. I’m in the empire business.",
    "We tried to poison you. We tried to poison you because you’re an insane, degenerate piece of filth, and you deserve to die.",
    "I watched Jane die. I was there. And I watched her die. I watched her overdose and choke to death. I could have saved her. But I didn’t.",
    "I told you Skyler, I warned you for a solid year: You cross me, and there will be consequences.",
    "Say my name.",
    "Stay out of my territory.",
    "My name is Walter Hartwell White. I live at 308 Negra Aroya Lane, Albuquerque, New Mexico, 87104.", 
    "To all law enforcement entities, this is not an admission of guilt. I am speaking to my family now.", 
    "Skyler, you are the love of my life. I hope you know that. Walter Jr., you’re my big man.", 
    "There are going to be some things that you’ll come to learn about me in the next few days.", 
    "But just know that no matter how it may look, I only had you in my heart. Goodbye.",
    "You need to stop focusing on the darkness behind you. The past is the past. Nothing can change what we’ve done.",
    "I’ve been living with cancer for the better part of a year. Right from the start it’s a death sentence.",
    "Every life comes with a death sentence.",  
    "But until then, who’s in charge? Me. That’s how I live my life.",
    "Electrons change their energy levels. Molecules change their bonds. Elements combine and change into compounds. That’s all of life. Its the constant. Its the cycle", 
    "It’s solution, dissolution, just over and over and over. It is growth, then decay, then transformation.",
    "There is gold in the streets just waiting for someone to come and scoop it up.",
    "I am the one who knocks.",
    "The universe is random, not inevitable. Its simple chaos",
    "I am not in danger. I am the danger",
    "Sometimes it just feels not to talk. At all. About anything. To anyone.",
    "You know, i just think that things have a way of working themselves out.",
    "Name one thing on this world that is not negotiable.",
    "We´re done when I say we´re donde",
    "You're an insane, degenerate piece of filth, and you deserve to die",
    "Chemistry is the study of matter. But I prefer to see it as the study of change",
    "I haven’t been myself lately, but I love you.",
    "You know, I’d appreciate it. I really would.",
    "Will you please, just once, get off my ass? You know, I’d appreciate it. I really would.",
    "I have spent my whole life scared. Frightened of things that could happen, might happen, might not happen.",
    "And I came to realize it’s that fear that’s the worst of it. That’s the real enemy.",
    "It cannot be blind luck or some imaginary relative who saves us. No, I earned that money, me",
    "There are two sides to every story, always.",
    "Let’s see, how should I put this? I’m in, you’re out",
    "Who are you talking to right now? Who is it you think you see? Do you know how much I make a year?",
    "No, you clearly don’t know who you’re talking to, so let me clue you in.",
    "What is going on with me is not about some disease, it’s about choices. Choices that I have made, choices I stand by.",
    "Never give up control. Live life on your own terms.",
    "I alone should suffer the consequences of those choices, no one else.",
    "We’re done when I say we’re done.",
    "It can be done exactly how I want it. The only question is, are you the man to do it?",
    ""
    
]


#frases = ["hola", "chau", "jajaja", "como estas", "kekekeke", "todo bien"]

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
        if 'walter' or "white" in mention.full_text.lower():
            print('found someone asking help...', flush=True)
            print('responding...', flush=True)
            api.update_status('@' + mention.user.screen_name + f" {res}", mention.id)

count = 1
while True:
    try:    
        hour = datetime.datetime.now().hour
        minutes = datetime.datetime.now().minute
        seconds = datetime.datetime.now().second
        word_day = random.choice(frases)
        api.update_status(str(count)+ ". " + word_day)
        count+=1
        reply_to_tweets()
        time.sleep(28800)
    except tweepy.TweepError as error:
        if error.api_code == 187:
            # Do something special
            print('duplicate message')
            api.update_status(str(count) + (word_day))
        else:
            raise error
        
        

while True:
    reply_to_tweets()
    time.sleep(15)

