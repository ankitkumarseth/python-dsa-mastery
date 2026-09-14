"""
LeetCode 242: Valid Anagram (Easy)

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""
import pytest

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass

# ==========================
# PYTEST SUITE
# ==========================
def test_standard():
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram") == True
    assert solution.isAnagram("rat", "car") == False

def test_edge_cases():
    solution = Solution()
    # Different lengths can never be anagrams
    assert solution.isAnagram("a", "ab") == False
    assert solution.isAnagram("", "") == True

def test_tle_large_input():
    # O(N log N) sorting is fine, but O(N) frequency map is better
    solution = Solution()
    s = "a" * 100000 + "b"
    t = "b" + "a" * 100000
    assert solution.isAnagram(s, t) == True
