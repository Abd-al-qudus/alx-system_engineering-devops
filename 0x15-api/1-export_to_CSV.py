#!/usr/bin/python3
'''This scripts gets an employee's todo list
   and return it using REST API'''
import csv
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
        user_data = []
        for data in resp:
            user_data.append([id, user_details.get('username'),
                             data.get('completed'), data.get('title')])
        with open('{}.csv'.format(id), 'w') as fob:
            writer = csv.writer(fob, quoting=csv.QUOTE_ALL)
            for row in user_data:
                writer.writerow(row)
