#!/usr/bin/python3
'''
Module containing a function that queries the Reddit API and prints the
titles of the first 10 hot posts for a given subreddit

Print None if an invalid subreddit is given
'''
import requests


def top_ten(subreddit):
    '''
    function queries the Reddit API and prints the titles of
    the first 10 host posts
    '''
    url = 'https://api.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'test_app'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return None

    try:
        data = response.json()

    except ValueError as e:
        print("JSON parse Error:\n", e)
        return None

    try:
        children = data.get('data').get('children')

        for child in children[:10]:
            print('{}'.format(child.get('data').get('title')))

    except Exception as e:
        print("Error:\n", e)
        return None
