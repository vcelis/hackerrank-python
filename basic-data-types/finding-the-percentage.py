#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Finding the percentage
Subdomain   :   Basic Data Types
Author      :   Vincent Celis
Created     :   18 July 2018

https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(format(sum(student_marks[query_name])/3.00, '.2f'))
