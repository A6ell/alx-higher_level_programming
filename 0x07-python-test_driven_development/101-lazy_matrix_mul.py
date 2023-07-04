#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Perform matrix multiplication using NumPy.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.
    """

    return np.matmul(m_a, m_b)
