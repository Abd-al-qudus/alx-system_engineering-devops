#!/usr/bin/python3
'''This scripts gets an employee's todo list
   and return it using REST API'''
import json
import requests as req
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: script <employee id>')
    else:
        id = argv[1]
        url = 'https://jsonplaceholder.typicode.com/users/{}/todos/'.format(id)
        user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
        resp = req.get(url).json()
        user_details = req.get(user_url).json()
        with open("{}.json".format(id), 'w') as json_file:
            user_data = list(map(
                    lambda x: {
                        "task": x.get("title"),
                        "completed": x.get("completed"),
                        "username": user_details.get('username')
                    },
                    resp
                ))
            user_data = {
                    "{}".format(id): user_data
            }
            json.dump(user_data, json_file)
