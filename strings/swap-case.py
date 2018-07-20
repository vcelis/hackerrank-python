#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   sWAP cASE
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/swap-case/problem
"""


def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
