class TwoPointers:
    """
    Practice fundamental Two Pointer patterns.
    """

    def is_palindrome(self, s: str) -> bool:
        """
        Given a string s, return True if it is a palindrome, or False otherwise.
        Only consider alphanumeric characters and ignore cases.
        """
        # TODO: Implement this using L and R pointers in O(N) time and O(1) space.
        left = 0
        right = len(s) - 1

        while left < right :
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and  not s[right].isalnum():
                right -=1

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                continue
            else:
                return False
        return True

    def two_sum_sorted(self, numbers: list[int], target: int) -> list[int]:
        """
        Given a 1-indexed array of integers sorted in non-decreasing order, 
        find two numbers that add up to target.
        Return the indices (1-indexed).
        """
        # TODO: Implement this using L and R pointers squeezing inwards. O(N) time, O(1) space.
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
        return None

