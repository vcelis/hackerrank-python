#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Find a string
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/find-a-string/problem
"""


def count_substring(string, sub_string):
    result = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            result += 1
    return result


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
