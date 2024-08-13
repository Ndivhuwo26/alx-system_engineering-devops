#!/usr/bin/python3

"""a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""

import requests
from sys import argv


def top_ten(subreddit):

    """Returns the top ten posts for a given subreddit"""
 
    user_agent = {'User-Agent': 'MyRedditScript/0.1 by /u/yourusername'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'

    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title'))
            else:
                print(None)
        else:
            print(None)
    except requests.RequestException:
        print(None)


if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Please provide a subreddit name.")

