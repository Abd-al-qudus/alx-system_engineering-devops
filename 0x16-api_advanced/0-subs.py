#!/usr/bin/python3
"""This script queries the reddit api and
    return the number of current users, returns 0
    if the subreddit is invalid
    Author : Engineer Phoenix
"""
import requests


def number_of_subscribers(subreddit):
    """takes a subreddit and return the total subscribers"""
    if not isinstance(subreddit, str) or subreddit is None:
        return 0
    headers = {'User-Agent': 'Engineer-Phoenix-0x16-advanced-API'}
    API = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(API, allow_redirects=False, headers=headers).json()
    return req.get('data', {}).get('subscribers', 0)
