#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Designer Door Mat
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/designer-door-mat/problem
"""


def print_mat(height, width):
    middle = (height - 1) / 2
    result = []
    for y in range(height):
        if y < middle:
            result.append(('.|.' * ((y * 2) + 1)).center(width, '-'))
        elif y == middle:
            result.append('WELCOME'.center(width, '-'))
    result.extend(result[:-1][::-1])

    for line in result:
        print(line)


if __name__ == '__main__':
    height, width = tuple([int(e) for e in input().split()])
    print_mat(height, width)
