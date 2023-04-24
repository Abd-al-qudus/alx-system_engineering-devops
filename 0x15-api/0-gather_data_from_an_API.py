#!/usr/bin/python3
'''This scripts gets an employee's todo list
   and return it using REST API'''
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
        completed = [userDict for userDict in resp
                     if userDict.get('completed')]
        print('Employee {} is done with tasks({}/{}):'
              .format(user_details.get('name'), len(completed), len(resp)))
        for user in completed:
            print('\t {}'.format(user.get('title')))
