#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   polar-coordinates
Subdomain   :   Math
Author      :   Vincent Celis
Created     :   05 September 2018

https://www.hackerrank.com/challenges/polar-coordinates/problem
"""

import cmath


def print_polar_coor(complex_number):
    r, y = cmath.polar(complex(complex_number))
    print(r)
    print(y)


if __name__ == '__main__':
    complex_number = str(input())
    print_polar_coor(complex_number)
