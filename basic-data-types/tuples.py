#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Tuples
Subdomain   :   Basic Data Types
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/python-tuples/problem
"""
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
