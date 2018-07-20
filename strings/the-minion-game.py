#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title       :   The Minion Game
Subdomain   :   Strings
Author      :   Vincent Celis
Created     :   19 July 2018

https://www.hackerrank.com/challenges/the-minion-game/problem
"""


def minion_game(string):
    # for char in word > remaning (including current) char in word = points
    points = {'Kevin': 0, 'Stuart': 0}
    for i, char in enumerate(string):
        if char in ['A', 'E', 'I', 'O', 'U']:
            points['Kevin'] += len(string) - i
        else:
            points['Stuart'] += len(string) - i

    result = 'Draw'
    if points['Kevin'] > points['Stuart']:
        result = '{} {}'.format('Kevin', points['Kevin'])
    elif points['Stuart'] > points['Kevin']:
        result = '{} {}'.format('Stuart', points['Stuart'])

    print(result)


if __name__ == '__main__':
    s = input()
    minion_game(s)
