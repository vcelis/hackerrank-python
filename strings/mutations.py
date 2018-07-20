#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Mutations
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/python-mutations/problem
"""


def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
