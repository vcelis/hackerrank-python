#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Merge the Tools!
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/merge-the-tools/problem
"""


def merge_the_tools(string, k):
    # Split string in segments of length k
    segments = [string[i:i+k] for i in range(0, len(string), k)]
    # Any duplicate occurrence of a char is removed from the string
    result = []
    for segment in segments:
        result.append(''.join([j for i, j in enumerate(segment)
                               if j not in segment[:i]]))
    print('\n'.join(result))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
