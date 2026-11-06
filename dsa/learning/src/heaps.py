import heapq
from collections import Counter

class Heaps:
    """
    Practice fundamental Heap and Priority Queue patterns.
    """

    def find_kth_largest(self, nums: list[int], k: int) -> int:
        """
        Given an integer array nums and an integer k, return the kth largest element.
        Use a min-heap of size k to achieve O(N log k) time.
        
        Example:
            nums = [3, 2, 1, 5, 6, 4], k = 2 -> 5
            nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4 -> 4
        """
        min_heap = []
        for x in nums:
            heapq.heappush(min_heap, x)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements.
        
        Example:
            nums = [1, 1, 1, 2, 2, 3], k = 2 -> [1, 2]
            nums = [1], k = 1 -> [1]
        """
        counts = Counter(nums)
        # Min-heap storing tuples: (frequency, num)
        min_heap = []
        for num, freq in counts.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for freq, num in min_heap]
