#!/usr/bin/python3
""" Defines a matrix division function """
def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        Matric list:A list of lists of integers or floats
        Div (int/float):The divisor
    Raises:
        TypeError:If the matrix contains non-numbers
        TypeError:If the matrix contains rows of different sizes
        TypeError:If div is not an int or float
        ZeroDivisionError:If div is 0
    Returns:
        A new matrix representing the result of the division
    """
    if (not isinstance(matrix, list) or matrix =[] or not )
