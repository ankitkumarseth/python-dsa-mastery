import pytest
from src.heaps import Heaps

class TestHeaps:

    def setup_method(self):
        self.sol = Heaps()

    def test_find_kth_largest(self):
        assert self.sol.find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
        assert self.sol.find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
        assert self.sol.find_kth_largest([1], 1) == 1

    def test_top_k_frequent(self):
        res = self.sol.top_k_frequent([1, 1, 1, 2, 2, 3], 2)
        assert set(res) == {1, 2}
        assert self.sol.top_k_frequent([1], 1) == [1]
