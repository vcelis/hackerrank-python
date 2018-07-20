#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Check Strict Superset
Subdomain   :   Sets
Author      :   Vincent Celis
Created     :   20 July 2018

https://www.hackerrank.com/challenges/py-check-strict-superset/problem
"""

if __name__ == '__main__':
    set_a = set(map(int, input().split()))
    n = int(input())
    result = True
    for _ in range(n):
        tmp = set(map(int, input().split()))
        if not set_a.issuperset(tmp):
            result = False
    print(result)
