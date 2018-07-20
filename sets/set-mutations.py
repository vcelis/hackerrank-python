#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Set Mutations
Subdomain   :   Sets
Author      :   Vincent Celis
Created     :   20 July 2018

https://www.hackerrank.com/challenges/py-set-mutations/problem
"""

methods = {
    'intersection_update': lambda *args: args[0].intersection_update(args[1]),
    'update': lambda *args: args[0].update(args[1]),
    'symmetric_difference_update': lambda *args: args[0].symmetric_difference_update(args[1]),
    'difference_update': lambda *args: args[0].difference_update(args[1])
}

if __name__ == '__main__':
    _ = input()
    set_one = set(map(int, input().split()))
    n = int(input())
    commands = [[[a for a in input().split()], [b for b in input().split()]]
                for _ in range(n)]

    for command in commands:
        method = methods[command[0][0]]
        method(set_one, set(map(int, command[1])))
    print(sum(set_one))
