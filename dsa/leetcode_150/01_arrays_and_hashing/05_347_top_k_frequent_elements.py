"""
LeetCode 347: Top K Frequent Elements (Medium)

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
"""
import pytest

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        pass

# ==========================
# PYTEST SUITE
# ==========================
def test_standard():
    solution = Solution()
    assert sorted(solution.topKFrequent([1,1,1,2,2,3], 2)) == [1, 2]
    assert solution.topKFrequent([1], 1) == [1]

def test_edge_cases():
    solution = Solution()
    # All same elements
    assert solution.topKFrequent([7,7,7,7,7], 1) == [7]
    # Negative elements
    assert sorted(solution.topKFrequent([-1,-1,2], 2)) == [-1, 2]

def test_tle_large_input():
    # O(N log N) sorting might be too slow compared to O(N) bucket sort
    solution = Solution()
    nums = [1] * 50000 + [2] * 40000 + [3] * 30000
    assert sorted(solution.topKFrequent(nums, 2)) == [1, 2]
