import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    cards = ['H2', 'SQ', 'DA', 'SJ', 'SK', 'C5', 'C10']
    assert solution.find_min_card(cards, 'S') == 'SJ'

def test_2():
    cards = ['HA', 'C3', 'H2', 'D4', 'H5', 'H8', 'S2']
    assert solution.find_min_card(cards, 'H') == 'H2'

def test_3():
    cards = ['DA', 'C8', 'H10', 'S4']
    assert solution.find_min_card(cards, 'C') == 'C8'
    cards = ['SA', 'C8', 'H10', 'C4']
    assert solution.find_min_card(cards, 'D') is None

def test_private():
    assert solution.find_min_card([], 'S') is None
