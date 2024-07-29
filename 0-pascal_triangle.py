#!/usr/bin/python3
'''Module to find Pascal's Triangle integers'''


def pascal_triangle(n):
    '''
    Function to find Pascal's Triangle integers

        Parameters:
            n (int): The number of row's of Pascal's triangle

        Returns:
            pascal_triangle (list): Binary string of the sum of a and b
    '''
    pascal_triangle = [[1]]

    for i in range(n - 1):
        temp = [0] + pascal_triangle[-1] + [0]
        row = []
        for j in range(len(pascal_triangle[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        pascal_triangle.append(row)
    return pascal_triangle
