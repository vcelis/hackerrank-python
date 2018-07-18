#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Find the Runner-Up Score!
Subdomain   :   Basic Data Types
Author      :   Vincent Celis
Created     :   18 July 2018

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""

if __name__ == '__main__':
    n = int(input())
    values = map(int, input().split())

    values = list(set(values))
    values.sort()
    print(values[-2])
