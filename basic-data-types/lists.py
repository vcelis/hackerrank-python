#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Lists
Subdomain   :   Basic Data Types
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/python-lists/problem
"""

methods = {
    'insert': lambda *args: args[0].insert(int(args[1]), int(args[2])),
    'print': lambda *args: print(args[0]),
    'remove': lambda *args: args[0].remove(int(args[1])),
    'append': lambda *args: args[0].append(int(args[1])),
    'sort': lambda *args: args[0].sort(),
    'pop': lambda *args: args[0].pop(),
    'reverse': lambda *args: args[0].reverse()
}

if __name__ == '__main__':
    N = int(input())
    commands = [[e for e in input().split()] for _ in range(N)]

    result = []
    for command in commands:
        method = methods[command[0]]
        method(result, *command[1:])
