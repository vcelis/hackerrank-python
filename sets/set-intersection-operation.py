#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Set .intersection() Operation
Subdomain   :   Sets
Author      :   Vincent Celis
Created     :   20 July 2018

https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
"""

if __name__ == '__main__':
    _ = input()
    set_one = set(map(int, input().split()))
    _ = input()
    set_two = set(map(int, input().split()))

    print(len(set_one.intersection(set_two)))
