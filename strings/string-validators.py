#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   String Validators
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/string-validators/problem
"""

if __name__ == '__main__':
    s = input()
    print(len(''.join(filter(lambda x: x.isalnum(), s))) > 0)
    print(len(''.join(filter(lambda x: x.isalpha(), s))) > 0)
    print(len(''.join(filter(lambda x: x.isnumeric(), s))) > 0)
    print(len(''.join(filter(lambda x: x.islower(), s))) > 0)
    print(len(''.join(filter(lambda x: x.isupper(), s))) > 0)
