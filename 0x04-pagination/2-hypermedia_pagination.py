#!/usr/bin/env python3
""" This module implements hypermedia pagination """
import csv
import math
from typing import List, Tuple
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initializes an instance of Server class """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Gets the correct page from the dataset and returns it """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()
        index_tuple: Tuple = index_range(page, page_size)
        start_index: int = index_tuple[0]
        end_index: int = index_tuple[1]
        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Gets the correct page from the dataset and returns dictionary """
        hyper_dict: dict = {}
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        page_result: List[List] = self.get_page(page, page_size)
        hyper_dict["page_size"] = len(page_result)
        hyper_dict["page"] = page
        hyper_dict["data"] = page_result
        if (page + 1) * page_size <= len(self.__dataset):
            hyper_dict["next_page"] = page + 1
        else:
            hyper_dict["next_page"] = None
        if (page - 1) * page_size >= 1:
            hyper_dict["prev_page"] = page - 1
        else:
            hyper_dict["prev_page"] = None
        hyper_dict["total_pages"] = math.ceil(len(self.__dataset) / page_size)
        return hyper_dict
