#!/usr/bin/python3
"""rotate an n x n 2D matrix 90 degrees clockwise'"""
import copy


def rotate_2d_matrix(matrix):
    '''rotate an n x n 2D matrix 90 degrees clockwise'''
    mxcopy = copy.deepcopy(matrix)
    nrows = len(matrix)
    ncols = len(matrix[0])
    row = mxcopy[nrows-1]
    c = 0
    for j in range(ncols):
        matrix[j][c] = row[j]
    for i in range(nrows-2, -1, -1):
        row = mxcopy[i]
        c = c + 1
        for j in range(ncols):
            matrix[j][c] = row[j]
