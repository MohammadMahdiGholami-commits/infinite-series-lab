import math 
from collections.abc import Callable

def partial_sum(
    term_function: Callable[[int], float],
    start: int,
    end: int,
) -> float:
    """
    Return the partial sum of a series from start to end.
    """
    if not callable(term_function):
        raise TypeError("term_function must be callable.")

    if (
        not isinstance(start, int)
        or isinstance(start, bool)
        or not isinstance(end, int)
        or isinstance(end, bool)
    ):
        raise TypeError("start and end must be integers.")

    if start < 0:
        raise ValueError("start must be non-negative.")

    if end < start:
        raise ValueError("end must be greater than or equal to start.")

    terms = (
        term_function(n)
        for n in range(start, end + 1)
    )

    return math.fsum(terms)

