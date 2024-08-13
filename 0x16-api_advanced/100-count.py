#!/usr/bin/python3

"""recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keyword"""

import requests
from collections import defaultdict

def count_words(subreddit, word_list, after="", word_count=None):
    """ this will recursively count keywords in titles of hot posts on a subreddit. """
    
    
    if word_count is None:
        word_count = defaultdict(int)
    
    
    word_list = [word.lower() for word in word_list]
    
    # Set up request parameters and headers
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    
  
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return  
        
        
        data = response.json().get('data', {})
        children = data.get('children', [])
        
     
        for child in children:
            title = child['data']['title'].lower().split()
            for word in word_list:
                word_count[word] += title.count(word)
        
        
        after = data.get('after')
        if after is not None:
            return count_words(subreddit, word_list, after, word_count)
        else:
            
            sorted_words = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_words:
                if count > 0:
                    print(f"{word}: {count}")
    
    except requests.RequestException:
        return  

