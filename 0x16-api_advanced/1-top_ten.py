#!/usr/bin/python3
"""This script queries the reddit api and
    print the first ten posts of the subreddit
    returns 0 if the subreddit is invalid
    Author : Engineer Phoenix
"""
import requests


def top_ten(subreddit):
    """takes a subreddit and print top ten post"""
    if not isinstance(subreddit, str) or subreddit is None:
        return None
    headers = {'User-Agent': 'Engineer-Phoenix-0x16-advanced-API'}
    API = "https://www.reddit.com/r/{}.json".format(subreddit)
    req = requests.get(API, allow_redirects=False, headers=headers,
                       params={'limit': 10}).json()
    responses = req.get('data', {}).get('children', [])
    if responses:
        [print(response.get('data').get('title'))
            for response in responses]
    else:
        print("None")
