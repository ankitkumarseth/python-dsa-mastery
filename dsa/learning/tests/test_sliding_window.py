import pytest
from src.sliding_window import SlidingWindow

class TestSlidingWindow:

    def setup_method(self):
        self.sol = SlidingWindow()

    def test_max_sub_array_of_size_k(self):
        assert self.sol.max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3) == 9
        assert self.sol.max_sub_array_of_size_k([2, 3, 4, 1, 5], 2) == 7
        assert self.sol.max_sub_array_of_size_k([1], 1) == 1
        assert self.sol.max_sub_array_of_size_k([], 2) == 0

    def test_longest_substring_without_repeating(self):
        assert self.sol.longest_substring_without_repeating("abcabcbb") == 3
        assert self.sol.longest_substring_without_repeating("bbbbb") == 1
        assert self.sol.longest_substring_without_repeating("pwwkew") == 3
        assert self.sol.longest_substring_without_repeating("") == 0
        assert self.sol.longest_substring_without_repeating("dvdf") == 3
