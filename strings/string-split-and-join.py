#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   String Split and Join
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/python-string-split-and-join/problem
"""


def split_and_join(line):
    return '-'.join(line.split())


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
