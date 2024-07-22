#!/usr/bin/env python3
"""This contains definition of index_range
helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This takes 2 integer arguments, returns a tuple of size two
    containing start and end index corresponding to the range of
    indexes to return in a list for pagination parameters
    Args:
        page (int): The page number to return (pages are 1-indexed)
        page_size (int): The number of items per page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
