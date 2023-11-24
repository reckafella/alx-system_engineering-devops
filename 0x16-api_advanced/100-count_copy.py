#!/usr/bin/python3
'''
Module contains a recursive function that queries the Reddit API, parses the\
        title of all hot articles, and prints a sorted count of given\
        keywords (case-insensitive, delimited by spaces
'''
from requests import get


def count_words(subreddit, word_list, after="", count_dic={}):
    '''
    a recursive function that queries the Reddit API, parses the title of all\
            hot articles, and prints a sorted count of given keywords\
            (case-insensitive, delimited by spaces
    '''

    if not count_dic:
        for word in word_list:
            count_dic[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in count_dic.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for w in word_list:
            if w[1]:
                print("{}: {}".format(w[0].lower(), w[1]))
        return None

    headers = {'user-agent': 'redditor'}
    params = {'after': after}
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)

    response = get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
    except Exception as e:
        return None

    try:
        data = data.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            title = post.get("title")
            lower = [s.lower() for s in title.split(' ')]

            for w in word_list:
                count_dic[w] += lower.count(w.lower())

    except Exception as e:
        return None

    count_words(subreddit, word_list, after, count_dic)
