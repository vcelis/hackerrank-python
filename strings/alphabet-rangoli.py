#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Alphabet Rangoli
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""

import string

alphabet = [char for char in string.ascii_lowercase]


def print_rangoli(size):
    result = []
    width = (size*2) - 1 + (size - 1) * 2
    for y in range(1, (size * 2)):
        if y < size:
            left = '-'.join(alphabet[size-1:size-y-1:-1])
            right = left[:len(left)-1][::-1]
            result.append((left + right).center(width, '-'))
        elif y == size:
            right = '-'.join(alphabet[:size])
            left = right[1:][::-1]
            result.append(left + right)

    result.extend(result[:-1][::-1])

    for line in result:
        print(line)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# print(y)
# print(y * 2 + 1 )
