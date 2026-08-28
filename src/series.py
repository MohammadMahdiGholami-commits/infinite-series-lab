"""
General-term functions for infinite series.
"""

import math


def geometric_term(n: int, a: float = 1.0, r: float = 0.5) -> float:
    """
    Return the n-th term of a geometric series.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")
    if n<1: 
        raise ValueError("n must be a positive integer")
    
    return a*(r**(n-1))

    
def harmonic_term(n: int) -> float:
    """
    Return the n-th term of the harmonic series.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be a positive integer.")

    return 1 / n

def p_series_term(n: int, p: float) -> float:
    """
    Return the n-th term of a p-series.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be a positive integer.")

    return 1 / (n ** p)

def exponential_term(n: int, x: float = 1.0) -> float:
    """
    Return the n-th term of the exponential series.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    return (x ** n) / math.factorial(n)
























