#!/usr/bin/python3
"""
This module '2-matrix_divided.py' divides elements of a matrix. 
Elements of the matrix will be either integers or floats, 
also elements of the same row will be of the same size.
"""
def matrix_divided(matrix, div):
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Add the rest of your code here
    if not all(len(row) == len(matrix[0]) for row in matrix):
      raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div,(int,float)):
       raise  TypeError("div must be a number")
    if div == 0:
       raise ZeroDivisionError("division by zero")
    
    return [[round(item / div, 2) for item in row] for row in matrix]
