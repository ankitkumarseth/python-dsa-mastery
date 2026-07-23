import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    data = [
        ('A', 500, 800),
        ('B', 1300, 1600),
        ('A', 2300, 2600),
        ('B', 3500, 3600),
        ('SPACE', 3700, 3800),
        ('SPACE', 3900, 4100),
        ('A', 4700, 4800),
        ('B', 5700, 5800),
        ('BACKSPACE', 6600, 6700),
        ('SPACE', 7600, 7900),
        ('BACKSPACE', 8300, 8500),
        ('A', 8700, 9000),
        ('B', 9200, 9400),
        ('SPACE', 10300, 10500),
        ('A', 10900, 11000),
        ('B', 11900, 12200),
    ]
    assert round(solution.average_hold_time(data, 'A'), 2) == 220.0
    assert round(solution.average_hold_time(data, 'B'), 2) == 200.0

def test_2():
    data = [
        ('A', 500, 800),
        ('B', 1300, 1600),
        ('A', 2300, 2600),
        ('B', 3500, 3600),
        ('SPACE', 3700, 3800),
        ('SPACE', 3900, 4100),
        ('A', 4700, 4800),
        ('B', 5700, 5800),
        ('BACKSPACE', 6600, 6700),
        ('SPACE', 7600, 7900),
        ('BACKSPACE', 8300, 8500),
        ('A', 8700, 9000),
        ('B', 9200, 9400),
        ('SPACE', 10300, 10500),
        ('A', 10900, 11000),
        ('B', 11900, 12200),
    ]
    assert round(solution.average_transition_time(data, 'A', 'B'), 2) == 680.0
    assert round(solution.average_transition_time(data, 'B', 'SPACE'), 2) == 500.0

def test_3():
    data = [
        ('A', 500, 800),
        ('B', 1300, 1600),
        ('A', 2300, 2600),
        ('B', 3500, 3600),
        ('SPACE', 3700, 3800),
        ('SPACE', 3900, 4100),
        ('A', 4700, 4800),
        ('B', 5700, 5800),
        ('BACKSPACE', 6600, 6700),
        ('SPACE', 7600, 7900),
        ('BACKSPACE', 8300, 8500),
        ('A', 8700, 9000),
        ('B', 9200, 9400),
        ('SPACE', 10300, 10500),
        ('A', 10900, 11000),
        ('B', 11900, 12200),
    ]
    assert solution.get_typed_text(data) == "ABAB  AAB AB"
    assert solution.get_typed_text(data[len(data)//2:]) == "AB AB"

def test_4():
    data = [
        ('A', 500, 800),
        ('B', 1300, 1600),
        ('A', 2300, 2600),
        ('B', 3500, 3600),
        ('SPACE', 3700, 3800),
        ('SPACE', 3900, 4100),
        ('A', 4700, 4800),
        ('B', 5700, 5800),
        ('BACKSPACE', 6600, 6700),
        ('SPACE', 7600, 7900),
        ('BACKSPACE', 8300, 8500),
        ('A', 8700, 9000),
        ('B', 9200, 9400),
        ('SPACE', 10300, 10500),
        ('A', 10900, 11000),
        ('B', 11900, 12200),
    ]
    assert round(solution.words_per_minute(data)) == 15
    assert round(solution.words_per_minute(data[len(data)//2:])) == 21
