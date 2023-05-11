#!/usr/bin/python3
"""This script queries the reddit API
    recursively and get the recent hot post
    Author - Engineer Phoenix
    """
import requests


def recurse(subreddit, hot_list=[], count=0, after=''):
    """get the hot list"""
    if not isinstance(subreddit, str) or subreddit is None:
        return None
    API = "https://www.reddit.com/r/{}.json".format(subreddit)
    header = {'User-Agent': 'Engr-phoenix'}
    param = {'limit': 100, 'count': count, 'after': after}
    resp = requests.get(API, headers=header, params=param,
                        allow_redirects=False)
    if resp.status_code == 400:
        return None
    resp = resp.json()
    after = resp.get('data', {}).get('after', "")
    count += resp.get('data', {}).get('dist', 0)
    for post in resp.get('data', {}).get('children', []):
        hot_list.append(post.get('data').get('title'))
    if after is not None:
        recurse(subreddit, hot_list, count, after)
    return hot_list
