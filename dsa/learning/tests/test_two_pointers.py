import pytest
from src.two_pointers import TwoPointers

class TestTwoPointers:
    
    def setup_method(self):
        self.sol = TwoPointers()

    def test_is_palindrome(self):
        assert self.sol.is_palindrome("A man, a plan, a canal: Panama") == True
        assert self.sol.is_palindrome("race a car") == False
        assert self.sol.is_palindrome(" ") == True

    def test_two_sum_sorted(self):
        assert self.sol.two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
        assert self.sol.two_sum_sorted([2, 3, 4], 6) == [1, 3]
        assert self.sol.two_sum_sorted([-1, 0], -1) == [1, 2]
