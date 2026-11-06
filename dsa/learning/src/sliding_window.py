class SlidingWindow:
    """
    Practice fundamental Sliding Window patterns (Fixed & Dynamic).
    """

    def max_sub_array_of_size_k(self, nums: list[int], k: int) -> int:
        """
        Given an array of integers and a number k, find the maximum sum of a contiguous subarray of size k.
        
        Example:
            nums = [2, 1, 5, 1, 3, 2], k = 3 -> 9 (subarray [5, 1, 3])
        """
        if not nums or k <= 0 or k > len(nums):
            return 0
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum

    def longest_substring_without_repeating(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without duplicate characters.
        
        Example:
            s = "abcabcbb" -> 3 ("abc")
            s = "bbbbb" -> 1 ("b")
            s = "pwwkew" -> 3 ("wke")
        """
        char_index = {}
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len
