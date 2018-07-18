#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Write a function
Subdomain   :   Introduction
Author      :   Vincent Celis
Created     :   18 July 2018

https://www.hackerrank.com/challenges/write-a-function/problem
"""


def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
