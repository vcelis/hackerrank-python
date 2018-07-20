#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   No Idea!
Subdomain   :   Sets
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/no-idea/problem
"""

from collections import Counter


def happiness(arr_one, set_one, set_two):
    score = Counter(arr_one)
    result = sum([score[num] for num in set_one.intersection(arr_one)])
    result -= sum([score[num] for num in set_two.intersection(arr_one)])
    return result


if __name__ == '__main__':
    _ = input()
    arr_one = list(map(int, input().split()))
    set_one = set(map(int, input().split()))
    set_two = set(map(int, input().split()))
    print(happiness(arr_one, set_one, set_two))
