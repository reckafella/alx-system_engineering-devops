#!/usr/bin/python3
'''
Module containing a function that queries the Reddit API and returns the
number of subscribers for a given subreddit.
If subreddit is given, the function returns 0
'''
import requests


def number_of_subscribers(subreddit):
    '''
    function that queries reddit API and returns number of subscribers
    '''
    URL = 'https://api.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'test_app'}

    response = requests.get(URL, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        data = data.get('data')
        return data.get('subscribers', 0)
    else:
        return 0
