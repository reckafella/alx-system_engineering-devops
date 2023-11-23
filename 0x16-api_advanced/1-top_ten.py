#!/usr/bin/python3
'''
Module containing a function that queries the Reddit API and prints the
titles of the first 10 hot posts for a given subreddit

Print None if an invalid subreddit is given
'''
from requests import get


def top_ten(subreddit):
    '''
    function queries the Reddit API and prints the titles of
    the first 10 hot posts
    '''

    headers = {'User-agent': 'Firefox Developer 118.0.2044.18'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return None

    results = response.json()

    try:
        data = results.get('data').get('children')

        for index in data:
            print(index.get('data').get('title'))

    except Exception:
        print(None)
        return None
