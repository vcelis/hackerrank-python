#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   What's Your Name?
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/whats-your-name/problem
"""


def print_full_name(a, b):
    print('Hello {} {}! You just delved into python.'.format(a, b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
