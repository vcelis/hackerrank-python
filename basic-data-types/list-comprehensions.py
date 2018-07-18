#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   List Comprehensions
Subdomain   :   Basic Data Types
Author      :   Vincent Celis
Created     :   18 July 2018

https://www.hackerrank.com/challenges/list-comprehensions/problem
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i, j, k] for i in range(x + 1) for j in range(y + 1)
          for k in range(z + 1) if i + j + k != n])
