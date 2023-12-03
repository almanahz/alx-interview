#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    if type(n) is not int or n <= 0:
        return triangle
    for number in range(n):
        row = 11 ** number
        number_list = list(map(int, str(row)))
        return number_list
