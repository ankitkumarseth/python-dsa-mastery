from collections import defaultdict, Counter
from typing import Any


class ArraysHashing:
    """
    Practice fundamental Array & Hashing patterns.
    These are modeled after classic NeetCode Easy problems.
    """

    def contains_duplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return True if any value appears at least twice.
        Return False if every element is distinct.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def is_anagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return True if t is an anagram of s.
        """
        if len(s) != len(t):
            return False

        # s_count = {}
        # t_count = {}
        # for i in range(len(s)):
        #     s_count[s[i]] = s_count.get(s[i], 0) + 1
        #     t_count[t[i]] = t_count.get(t[i], 0) + 1
        # return s_count == t_count

        # Using Default Dict: Handles missing key with 0
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        for i in range(len(s)):
            s_count[s[i]] += 1
            t_count[t[i]] += 1
        return s_count == t_count

        # Using Built-in Counter. Pythonic, but hides the underlying logic. O(N) Time.
        # return Counter(s) == Counter(t)

        # Using Sorting: No HashMap needed, but slower due to sorting. O(N log N) Time.
        # return sorted(s) == sorted(t)



    def two_sum_one_pair(self, nums: list[int], target: int) -> list[int] | None:
        """
        Given an array of integers nums and an integer target, return indices 
        of the two numbers such that they add up to target.
        """
        num_map = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in num_map:
                return [num_map[needed], i]
            num_map[num] = i
        return None

    def two_sum_all_pairs(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Given an array of integers nums and an integer target, return indices
        of the two numbers such that they add up to target.
        """
        num_map = {}
        all_pairs = []
        for i, num in enumerate(nums):
            needed = target - num
            if needed in num_map:
                all_pairs.append([num_map[needed], i])
            num_map[num] = i
        return all_pairs


