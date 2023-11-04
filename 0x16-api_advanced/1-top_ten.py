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
    url = 'https://api.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'test_app'}
    params = {'limit': 100}

    response = requests.get(url, params=params,
                            headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data.get('data').get('children')

        for child in children[:10]:
            title = child.get('data').get('title')
            print(title)
    else:
        print("None")
