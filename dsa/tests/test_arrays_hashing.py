import pytest
from src.arrays_hashing import ArraysHashing

class TestArraysHashing:
    
    def setup_method(self):
        self.sol = ArraysHashing()

    def test_contains_duplicate(self):
        assert self.sol.contains_duplicate([1, 2, 3, 1]) == True
        assert self.sol.contains_duplicate([1, 2, 3, 4]) == False
        assert self.sol.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

    def test_is_anagram(self):
        assert self.sol.is_anagram("anagram", "nagaram") == True
        assert self.sol.is_anagram("rat", "car") == False
        assert self.sol.is_anagram("a", "ab") == False

    def test_two_sum_one_pair(self):
        assert self.sol.two_sum_one_pair([2, 7, 11, 15], 9) in ([0, 1], [1, 0])
        assert self.sol.two_sum_one_pair([3, 2, 4], 6) in ([1, 2], [2, 1])
        assert self.sol.two_sum_one_pair([3, 3], 6) in ([0, 1], [1, 0])

    def test_two_sum_all_pairs(self):
        assert self.sol.two_sum_all_pairs([2, 7, 4, 11, 3, 15, 6, 5], 9) == [[0, 1], [4, 6], [2, 7]]
