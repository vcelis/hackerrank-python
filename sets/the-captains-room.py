#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   The Captain's Room
Subdomain   :   Sets
Author      :   Vincent Celis
Created     :   20 July 2018

https://www.hackerrank.com/challenges/py-the-captains-room/problem
"""

if __name__ == '__main__':
    k = int(input())
    room_numbers = list(map(int, input().split()))
    print(int(((sum(set(room_numbers)) * k) - sum(room_numbers)) / (k - 1)))
