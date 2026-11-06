import pytest
from src.intervals import Intervals

class TestIntervals:

    def setup_method(self):
        self.sol = Intervals()

    def test_merge_intervals(self):
        assert self.sol.merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
        assert self.sol.merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
        assert self.sol.merge_intervals([[1, 4], [0, 4]]) == [[0, 4]]
        assert self.sol.merge_intervals([]) == []

    def test_can_attend_meetings(self):
        assert self.sol.can_attend_meetings([[0, 30], [5, 10], [15, 20]]) == False
        assert self.sol.can_attend_meetings([[7, 10], [2, 4]]) == True
        assert self.sol.can_attend_meetings([[1, 5], [5, 10]]) == True
