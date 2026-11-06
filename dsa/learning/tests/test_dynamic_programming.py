import pytest
from src.dynamic_programming import DynamicProgramming

class TestDynamicProgramming:

    def setup_method(self):
        self.sol = DynamicProgramming()

    def test_climb_stairs(self):
        assert self.sol.climb_stairs(1) == 1
        assert self.sol.climb_stairs(2) == 2
        assert self.sol.climb_stairs(3) == 3
        assert self.sol.climb_stairs(4) == 5
        assert self.sol.climb_stairs(5) == 8

    def test_coin_change(self):
        assert self.sol.coin_change([1, 2, 5], 11) == 3
        assert self.sol.coin_change([2], 3) == -1
        assert self.sol.coin_change([1], 0) == 0
        assert self.sol.coin_change([2, 5, 10, 1], 27) == 4  # 10 + 10 + 5 + 2
