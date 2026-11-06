import pytest
from src.bit_manipulation import BitManipulation

class TestBitManipulation:

    def setup_method(self):
        self.sol = BitManipulation()

    def test_single_number(self):
        assert self.sol.single_number([2, 2, 1]) == 1
        assert self.sol.single_number([4, 1, 2, 1, 2]) == 4
        assert self.sol.single_number([1]) == 1

    def test_count_set_bits(self):
        assert self.sol.count_set_bits(11) == 3   # binary 1011
        assert self.sol.count_set_bits(128) == 1  # binary 10000000
        assert self.sol.count_set_bits(0) == 0
        assert self.sol.count_set_bits(7) == 3    # binary 111
