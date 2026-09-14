"""
LeetCode 217: Contains Duplicate (Easy)

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""
import pytest

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        pass

# ==========================
# PYTEST SUITE
# ==========================
def test_standard():
    solution = Solution()
    assert solution.containsDuplicate([1, 2, 3, 1]) == True
    assert solution.containsDuplicate([1, 2, 3, 4]) == False
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

def test_edge_cases():
    solution = Solution()
    assert solution.containsDuplicate([]) == False  # Empty array
    assert solution.containsDuplicate([5]) == False # Single element

def test_tle_large_input():
    # O(N^2) naive loop will hang here
    solution = Solution()
    nums = list(range(100000)) + [99999]
    assert solution.containsDuplicate(nums) == True
