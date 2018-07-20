#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Introduction to Sets
Subdomain   :   Sets
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
"""


def average(array):
    my_set = set(array)
    return sum(my_set) / len(my_set)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
