"""
LeetCode 1: Two Sum (Easy)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
import pytest

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pass

# ==========================
# PYTEST SUITE
# ==========================
def test_standard():
    solution = Solution()
    assert sorted(solution.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(solution.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(solution.twoSum([3, 3], 6)) == [0, 1]

def test_edge_cases():
    solution = Solution()
    # Negative numbers
    assert sorted(solution.twoSum([-1, -2, -3, -4, -5], -8)) == [2, 4]

def test_tle_large_input():
    # O(N^2) double loop will hang here
    solution = Solution()
    nums = list(range(10000, 110000)) # 100,000 elements
    # Target requires the first and last elements
    target = nums[0] + nums[-1]
    assert sorted(solution.twoSum(nums, target)) == [0, len(nums)-1]
