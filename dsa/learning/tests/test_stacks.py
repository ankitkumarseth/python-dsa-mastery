import pytest
from src.stacks import Stacks

class TestStacks:

    def setup_method(self):
        self.sol = Stacks()

    def test_is_valid_parentheses(self):
        assert self.sol.is_valid_parentheses("()") == True
        assert self.sol.is_valid_parentheses("()[]{}") == True
        assert self.sol.is_valid_parentheses("(]") == False
        assert self.sol.is_valid_parentheses("([)]") == False
        assert self.sol.is_valid_parentheses("{[]}") == True
        assert self.sol.is_valid_parentheses("") == True

    def test_next_greater_element(self):
        assert self.sol.next_greater_element([4, 5, 2, 25]) == [5, 25, 25, -1]
        assert self.sol.next_greater_element([13, 7, 6, 12]) == [-1, 12, 12, -1]
        assert self.sol.next_greater_element([1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1]
        assert self.sol.next_greater_element([5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
