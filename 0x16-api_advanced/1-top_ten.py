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
    the first 10 hot posts
    '''
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'personal app'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)

    try:
        data = response.json()

    except ValueError as error:
        print(None)

    try:
        data = data.get('data')
        children = data.get('children')

        for child in children[:10]:
            title = child.get('data').get('title')
            print(title)

    except Exception as error:
        print(None)
