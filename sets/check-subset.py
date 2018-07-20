#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Check Subset
Subdomain   :   Sets
Author      :   Vincent Celis
Created     :   20 July 2018

https://www.hackerrank.com/challenges/py-check-subset/problem
"""

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        _ = input()
        set_one = set(input().split())
        _ = input()
        set_two = set(input().split())
        print(set_one.issubset(set_two))
