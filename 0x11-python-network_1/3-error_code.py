#!/usr/bin/python3
"""A Python script that displays the body of the response"""
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as err:
        print('Error code:', err.code)
