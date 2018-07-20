#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   String Formatting
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/python-string-formatting/problem
"""


def print_formatted(number):
    for i in range(1, number+1):
        print("{0:>{1}d} {0:>{1}o} {0:>{1}X} {0:>{1}b}"
              .format(i, len(bin(number))-2))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
