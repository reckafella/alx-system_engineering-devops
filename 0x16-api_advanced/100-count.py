#!/usr/bin/python3
'''
Module contains a recursive function that queries the Reddit API, parses the\
        title of all hot articles, and prints a sorted count of given\
        keywords (case-insensitive, delimited by spaces
'''
from requests import get


def count_words(subreddit, word_list, after=None, count=[]):
    '''
    a recursive function that queries the Reddit API, parses the title of all\
            hot articles, and prints a sorted count of given keywords\
            (case-insensitive, delimited by spaces
    '''
    if after is None:
        count = [0] * len(word_list)

    headers = {'user-agent': 'redditor'}
    params = {'after': after}
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)

    response = get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
    except Exception:
        return None

    for title in (data['data']['children']):
        for word in title['data']['title'].split():
            for i in range(len(word_list)):
                if word_list[i].lower() == word.lower():
                    count[i] += 1

    after = data.get('data').get('after')

    if after is not None:
        count_words(subreddit, word_list, after, count)
    else:
        save = []
        for i in range(len(word_list)):
            for j in range(i + 1, len(word_list)):
                if word_list[i].lower() == word_list[j].lower():
                    save.append(j)
                    count[i] += count[j]

        for i in range(len(word_list)):
            for j in range(i, len(word_list)):
                if (count[j] > count[i] or (word_list[i] > word_list[j] and
                                            count[j] == count[i])):
                    temp = count[i]
                    count[i] = count[j]
                    count[j] = temp

                    temp = word_list[i]
                    word_list[i] = word_list[j]
                    word_list[j] = temp

        for i in range(len(word_list)):
            if (count[i] > 0 and i not in save):
                print("{}: {}".format(word_list[i].lower(), count[i]))
