"""
LeetCode 238: Product of Array Except Self (Medium)

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""
import pytest

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pass

# ==========================
# PYTEST SUITE
# ==========================
def test_standard():
    solution = Solution()
    assert solution.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert solution.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

def test_edge_cases():
    solution = Solution()
    assert solution.productExceptSelf([0, 0]) == [0, 0] # Multiple zeros
    assert solution.productExceptSelf([1, 0]) == [0, 1] # Single zero

def test_tle_large_input():
    # O(N^2) solution will fail here
    solution = Solution()
    nums = [1] * 100000
    assert len(solution.productExceptSelf(nums)) == 100000
