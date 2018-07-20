#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Capitalize!
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/capitalize/problem
"""

import math
import os
import random
import re
import sys


def solve(s):
    return ' '.join([char[0].upper() + char[1:] if char.isalpha() else char
                    for char in s.split(' ')])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
