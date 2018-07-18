#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   Nested Lists
Subdomain   :   Basic Data Types
Author      :   Vincent Celis
Created     :   18 July 2018

https://www.hackerrank.com/challenges/nested-list/problem
"""
if __name__ == '__main__':
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])

    # Find second lowest score by creating a set of scores and taking second
    second_lowest_score = list(set([grade[1] for grade in grades]))
    second_lowest_score.sort()
    second_lowest_score = second_lowest_score[1]

    # Make a list of student names if the have the second lowest score
    result = [student[0] for student in grades
              if student[1] == second_lowest_score]
    # Sort and print that list
    result.sort()
    print('\n'.join(result))
