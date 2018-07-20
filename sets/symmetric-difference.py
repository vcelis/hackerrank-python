#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Symmetric Difference
Subdomain   :   Sets
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/symmetric-difference/problem
"""


def sym_diff(arr_one, arr_two):
    result = set(arr_one).symmetric_difference(set(arr_two))
    result = list(result)
    result.sort()
    print('\n'.join(str(r) for r in result))


if __name__ == '__main__':
    _ = input()
    arr_one = list(map(int, input().split()))
    _ = input()
    arr_two = list(map(int, input().split()))
    sym_diff(arr_one, arr_two)
