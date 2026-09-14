"""
LeetCode 128: Longest Consecutive Sequence (Medium)

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""
import pytest

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        pass

# ==========================
# PYTEST SUITE
# ==========================
def test_standard():
    solution = Solution()
    assert solution.longestConsecutive([100,4,200,1,3,2]) == 4
    assert solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9

def test_edge_cases():
    solution = Solution()
    assert solution.longestConsecutive([]) == 0
    assert solution.longestConsecutive([1,1,1,1]) == 1 # Duplicates shouldn't count extra

def test_tle_large_input():
    # O(N log N) sorting is usually accepted by LC, but O(N) hash set is required for true optimal
    # An O(N^2) naive loop will hang here
    solution = Solution()
    nums = list(range(100000))
    nums.reverse() # Worst case for naive iteration
    assert solution.longestConsecutive(nums) == 100000
