#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Set .discard(), .remove() & .pop()
Subdomain   :   Sets
Author      :   Vincent Celis
Created     :   20 July 2018

https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
"""


methods = {
    'remove': lambda *args: args[0].remove(int(args[1])),
    'discard': lambda *args: args[0].discard(int(args[1])),
    'pop': lambda *args: args[0].pop()
}


if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    c = int(input())
    commands = [[e for e in input().split()] for _ in range(c)]

    for command in commands:
        method = methods[command[0]]
        method(s, *command[1:])
    print(sum(s))
