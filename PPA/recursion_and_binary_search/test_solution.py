import os
import importlib.util
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)


def test_triangular():
    assert solution.triangular(5) == 15
    assert solution.triangular(10) == 55
    assert solution.triangular(1) == 1

def test_factorial():
    assert solution.factorial(3) == 6
    assert solution.factorial(5) == 120
    assert solution.factorial(1) == 1

def test_multiply():
    assert solution.multiply(2, 3) == 6
    assert solution.multiply(5, 4) == 20
    assert solution.multiply(10, 10) == 100

def test_logarithm():
    assert solution.logarithm(4) == 2
    assert solution.logarithm(16) == 4
    assert solution.logarithm(1) == 0

def test_palindrome():
    assert solution.palindrome("mom") is True
    assert solution.palindrome("random") is False
    assert solution.palindrome("racecar") is True

def test_spiral_iterative():
    # Floating point comparisons should use pytest.approx
    assert solution.spiral_iterative(0, 1, 4) == pytest.approx(0.625)
    assert solution.spiral_iterative(0, 1, 100) == pytest.approx(0.666666, abs=1e-3)

def test_spiral_recursive():
    assert solution.spiral_recursive(0, 1, 4) == pytest.approx(0.625)
    assert solution.spiral_recursive(0, 1, 100) == pytest.approx(0.666666, abs=1e-3)

def test_count():
    assert solution.count(['good', 'string', 'good', 'again', 'good'], 'good') == 3
    assert solution.count(['a', 'small', 'big', 'a', 'the'], 'small') == 1
    assert solution.count(['a', 'b', 'c'], 'z') == 0

def test_non_decreasing():
    assert solution.non_decreasing([1, 10, 100, 1000]) is True
    assert solution.non_decreasing([10, 1, 100, 1000, 10000]) is False
    assert solution.non_decreasing([1, 1, 2, 3, 3, 5]) is True

def test_uniq():
    assert solution.uniq([1, 2, 3, 2, 1, 4]) == [3, 2, 1, 4]
    assert solution.uniq([10, 9, 6, 9, 10, 6, 10]) == [9, 6, 10]
    assert solution.uniq([1, 1, 1]) == [1]

def test_search():
    assert solution.search([1, 2, 3, 4], 2) is True
    assert solution.search([10, 20, 30, 40, 50], 15) is False
    assert solution.search([], 1) is False

def test_insert():
    assert solution.insert([1, 2, 3, 5], 4) == [1, 2, 3, 4, 5]
    assert solution.insert([1, 2], 0) == [0, 1, 2]

def test_isort():
    assert solution.isort([1, 5, 4, 3, 2]) == [1, 2, 3, 4, 5]
    assert solution.isort([10, 1, 9, 2]) == [1, 2, 9, 10]

def test_poly():
    assert solution.poly([1, 2, 3], 5) == 86
    assert solution.poly([1, -2, 3, 4], 10) == 4281

def test_power():
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_3 = [[468, 576, 684], [1062, 1305, 1548], [1656, 2034, 2412]]
    assert solution.power(A, 3) == expected_3

    A2 = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
    expected_2 = [[30, 36, 45], [66, 81, 102], [109, 134, 169]]
    assert solution.power(A2, 2) == expected_2

def test_subset_sum():
    assert solution.subset_sum([1, 2, 3, 4, 5], 6) is True
    assert solution.subset_sum([1, 9, 10, 5, 8, 13], 26) is True
    assert solution.subset_sum([1, 49, 29, 13, 95, 32, 10, 1, 5], 21) is False
    assert solution.subset_sum([1, 49, 29, 13, 95, 32, 10, 1, 5], 20) is True
