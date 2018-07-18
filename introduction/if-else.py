#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Python If-Else
Subdomain   :   Introduction
Author      :   Vincent Celis
Created     :   18 July 2018

https://www.hackerrank.com/challenges/py-if-else/problem
"""

if __name__ == '__main__':
    num = int(input())
    if num % 2 != 0:
        print('Weird')
    else:
        if num in range(2, 6) or num > 20:
            print('Not Weird')
        else:
            print('Weird')
