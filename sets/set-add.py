#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Set .add()
Subdomain   :   Sets
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/py-set-add/problem
"""


if __name__ == '__main__':
    n = int(input())
    my_set = set(input() for _ in range(n))
    print(len(my_set))
