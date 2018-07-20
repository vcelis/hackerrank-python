#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Set .symmetric_difference() Operation
Subdomain   :   Sets
Author      :   Vincent Celis
Created     :   20 July 2018

https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
"""

if __name__ == '__main__':
    _ = input()
    set_one = set(map(int, input().split()))
    _ = input()
    set_two = set(map(int, input().split()))

    print(len(set_one.symmetric_difference(set_two)))
