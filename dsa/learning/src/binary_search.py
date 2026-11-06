class BinarySearch:
    """
    Practice fundamental Binary Search patterns.
    """

    def search(self, nums: list[int], target: int) -> int:
        """
        Given a sorted array of distinct integers in ascending order and a target value,
        return the index if target is found. Otherwise return -1.
        
        Example:
            nums = [-1, 0, 3, 5, 9, 12], target = 9 -> 4
            nums = [-1, 0, 3, 5, 9, 12], target = 2 -> -1
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search_insert_position(self, nums: list[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value,
        return the index if the target is found. If not, return the index
        where it would be if it were inserted in order.
        
        Example:
            nums = [1, 3, 5, 6], target = 5 -> 2
            nums = [1, 3, 5, 6], target = 2 -> 1
            nums = [1, 3, 5, 6], target = 7 -> 4
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
