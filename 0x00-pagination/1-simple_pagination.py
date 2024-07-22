#!/usr/bin/env python3
"""This defines class Server that paginates a database
of popular baby names"""
import csv
import math
from typing import List, Tuple


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


class Server:
    """THe server class to paginate database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This takes 2 integer arguments, returns requested page from dataset
        Args:
            page (int): The required page number, must be positive integer
            page_size (int): The size of records per page, must be positve int
        Return:
            The lists containing required data from dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        data_length = len(dataset)
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []
