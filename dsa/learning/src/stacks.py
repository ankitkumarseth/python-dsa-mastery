class Stacks:
    """
    Practice fundamental Stack and Monotonic Stack algorithms.
    """

    def is_valid_parentheses(self, s: str) -> bool:
        """
        Given a string s containing '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.
        
        Example:
            s = "()[]{}" -> True
            s = "(]" -> False
        """
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

    def next_greater_element(self, nums: list[int]) -> list[int]:
        """
        Given an array of integers, find the Next Greater Element for each element.
        If no greater element exists to its right, output -1 for that element.
        
        Example:
            nums = [4, 5, 2, 25] -> [5, 25, 25, -1]
            nums = [13, 7, 6, 12] -> [-1, 12, 12, -1]
        """
        n = len(nums)
        result = [-1] * n
        stack = []  # indices of elements waiting for next greater
        for i, val in enumerate(nums):
            while stack and nums[stack[-1]] < val:
                prev_idx = stack.pop()
                result[prev_idx] = val
            stack.append(i)
        return result
