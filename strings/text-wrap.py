#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Text Wrap
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/text-wrap/problem
"""

import textwrap


def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)