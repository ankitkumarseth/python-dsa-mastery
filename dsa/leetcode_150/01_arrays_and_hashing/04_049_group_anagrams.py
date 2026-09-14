"""
LeetCode 49: Group Anagrams (Medium)

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""
from collections import defaultdict
import pytest


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # TODO: Implement solution
        pass


# ==========================
# PYTEST SUITE
# ==========================
def test_standard_case():
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    # We sort the sublists and the outer list to ensure order-agnostic comparison
    result = solution.groupAnagrams(strs)
    result = sorted([sorted(sub) for sub in result])
    
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    expected = sorted([sorted(sub) for sub in expected])
    
    assert result == expected

def test_empty_string():
    solution = Solution()
    assert solution.groupAnagrams([""]) == [[""]]

def test_single_character():
    solution = Solution()
    assert solution.groupAnagrams(["a"]) == [["a"]]

def test_tle_large_input():
    # To test Time Limit Exceeded locally. 
    # Create an array of 10,000 identical strings.
    # An O(N^2) solution will hang here.
    solution = Solution()
    strs = ["a"] * 10000
    
    result = solution.groupAnagrams(strs)
    assert len(result) == 1
    assert len(result[0]) == 10000
