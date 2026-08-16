import os
import importlib.util

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)


def test_reverse():
    assert solution.reverse([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert solution.reverse([10, 5, 1, 4, 9]) == [9, 4, 1, 5, 10]
    assert solution.reverse(['a', 'b', 'c', 'd', 'e', 'f']) == ['f', 'e', 'd', 'c', 'b', 'a']
    # Edge cases
    assert solution.reverse([]) == []
    assert solution.reverse([1]) == [1]


def test_linear():
    assert solution.linear([2, 4, 6, 8], [1, 2, 3, 4], 2) is True
    assert solution.linear([10, 20, 30, 40, 50], [1, 2, 3, 4, 6], 10) is False
    # Edge case: Different lengths
    assert solution.linear([2, 4], [1, 2, 3], 2) is False
    assert solution.linear([2, 4, 6], [1, 2], 2) is False


def test_collatz():
    assert solution.collatz(7) == 16
    assert solution.collatz(10) == 6
    assert solution.collatz(101) == 25
    # Edge case: Already at 1
    assert solution.collatz(1) == 0


def test_steps():
    assert solution.steps(1) == 1
    assert solution.steps(2) == 2
    assert solution.steps(3) == 4
    assert solution.steps(5) == 13
    assert solution.steps(6) == 24


def test_ancestry():
    P1 = {'Jahangir': 'Akbar', 'Akbar': 'Humayun', 'Humayun': 'Babur'}
    assert solution.ancestry(P1, 'Jahangir', 'Babur') == ['Jahangir', 'Akbar', 'Humayun', 'Babur']

    P2 = {'Anil': 'Krishna', 'Mohan': 'Prasanna', 'Krishna': 'Prasanna', 'Prasanna': 'Mukesh'}
    assert solution.ancestry(P2, 'Anil', 'Prasanna') == ['Anil', 'Krishna', 'Prasanna']
    assert solution.ancestry(P2, 'Mohan', 'Mukesh') == ['Mohan', 'Prasanna', 'Mukesh']
