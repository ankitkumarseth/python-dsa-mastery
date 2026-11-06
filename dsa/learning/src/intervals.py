class Intervals:
    """
    Practice fundamental Interval scheduling and merging algorithms.
    """

    def merge_intervals(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Given an array of intervals where intervals[i] = [start_i, end_i],
        merge all overlapping intervals.
        
        Example:
            intervals = [[1, 3], [2, 6], [8, 10], [15, 18]] -> [[1, 6], [8, 10], [15, 18]]
            intervals = [[1, 4], [4, 5]] -> [[1, 5]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

    def can_attend_meetings(self, intervals: list[list[int]]) -> bool:
        """
        Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
        determine if a person could attend all meetings.
        
        Example:
            intervals = [[0, 30], [5, 10], [15, 20]] -> False
            intervals = [[7, 10], [2, 4]] -> True
        """
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
