import praw
import pandas as pd
import os
from urllib import request

def getSubData(range_,subreddit_):

    posts = []
    pd.options.display.width = 0
    pd.set_option('display.max_rows', None)

    reddit = praw.Reddit(client_id='2gRnB9ug0iK4pA', client_secret='j-WcUToQeR_86uoVnycFytIWpnymBg', user_agent='ScrapingReddit')

    ml_subreddit = reddit.subreddit(subreddit_)
    for post in ml_subreddit.hot(limit=range_):
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

    posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

    posts.to_csv(r'C:\Users\Lasse Thamsen\Documents\Pythondata\reddit1.csv', index=False, header=True)

    posts.sort_values(by=['score'], inplace=True, ascending = False)

    print(posts)

    return posts
def savePhotos(posts_):

    range_=len(posts_)

    for x in range(range_):

        URL = posts_.iloc[x]['url']

        if URL.endswith('jpg'):
            i = 0
            while os.path.exists(r"C:\Users\Lasse Thamsen\Documents\Pythondata\pics\sample%s.jpg" % i):
                i += 1
            try: 
                request.urlretrieve(URL, r"C:\Users\Lasse Thamsen\Documents\Pythondata\pics\sample%s.jpg" % i)
            except: 
                print('error')
        if URL.endswith('png'):
            i = 0
            while os.path.exists(r"C:\Users\Lasse Thamsen\Documents\Pythondata\pics\sample%s.png" % i):
                i += 1
            try:
                request.urlretrieve(URL, r"C:\Users\Lasse Thamsen\Documents\Pythondata\pics\sample%s.png" % i)
            except:
                print('error')
