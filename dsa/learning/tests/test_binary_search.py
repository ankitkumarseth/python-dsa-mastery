import pytest
from src.binary_search import BinarySearch

class TestBinarySearch:

    def setup_method(self):
        self.sol = BinarySearch()

    def test_search(self):
        assert self.sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
        assert self.sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
        assert self.sol.search([5], 5) == 0
        assert self.sol.search([5], -5) == -1
        assert self.sol.search([], 1) == -1

    def test_search_insert_position(self):
        assert self.sol.search_insert_position([1, 3, 5, 6], 5) == 2
        assert self.sol.search_insert_position([1, 3, 5, 6], 2) == 1
        assert self.sol.search_insert_position([1, 3, 5, 6], 7) == 4
        assert self.sol.search_insert_position([1, 3, 5, 6], 0) == 0
