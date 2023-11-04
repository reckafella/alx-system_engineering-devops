#!/usr/bin/python3
"""
Module contains a recursive function that queries the Reddit API and returns\
    a list containing the titles of all hot articles for a given subreddit.\
        If no results are found for the given subreddit,\
            the function should return None.
"""
import requests as r


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list\
        containing the titles of all hot articles for a given subreddit.\
            If no results are found for the given subreddit,\
                the function should return None.
    """
    url = 'https://api.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {
        'user-agent': 'test_app'
        }
    params = {
        'limit': 100,
        'after': after
    }
    response = r.get(url, params=params,
                     headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        _after = data.get('data').get('after')
        children = data.get('data').get('children')

        for child in children:
            hot_list.append(child.get('data').get('title'))

        if (_after is not None):
            recurse(subreddit, hot_list, after=_after)
        return hot_list
    else:
        return None
