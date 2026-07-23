import subprocess
import os

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def run_script(input_text):
    result = subprocess.run(
        ["python3", SOLUTION_FILE],
        input=input_text,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()

# --- Permutation ---


def test_permutation_tc1():
    assert run_script("permutation\nabc\n") == "ab\nac\nba\nbc\nca\ncb"

def test_permutation_tc2():
    assert run_script("permutation\ndog\n") == "do\ndg\nod\nog\ngd\ngo"

def test_permutation_edge():
    assert run_script("permutation\nxy\n") == "xy\nyx"

# --- Sorted Permutation ---


def test_sorted_permutation_tc3():
    assert run_script("sorted_permutation\nbca\n") == "bc\nab\nac"

def test_sorted_permutation_tc4():
    assert run_script("sorted_permutation\nbad\n") == "bd\nab\nad"

# --- Repeat the Repeat ---


def test_repeat_the_repeat_tc5():
    assert run_script("repeat_the_repeat\n3\n") == "123\n123\n123"

def test_repeat_the_repeat_tc6():
    assert run_script("repeat_the_repeat\n4\n") == "1234\n1234\n1234\n1234"

def test_repeat_the_repeat_edge():
    # n = 1 should just print 1 once
    assert run_script("repeat_the_repeat\n1\n") == "1"

# --- Repeat Incrementally ---


def test_repeat_incrementally_tc7():
    assert run_script("repeat_incrementally\n4\n") == "1\n12\n123\n1234"

def test_repeat_incrementally_tc8():
    assert run_script("repeat_incrementally\n5\n") == "1\n12\n123\n1234\n12345"

# --- Increment and Decrement ---


def test_increment_and_decrement_tc9():
    assert run_script("increment_and_decrement\n3\n") == "1\n121\n12321"

def test_increment_and_decrement_tc10():
    assert run_script("increment_and_decrement\n4\n") == "1\n121\n12321\n1234321"

def test_increment_and_decrement_edge():
    # n = 1 should just print 1
    assert run_script("increment_and_decrement\n1\n") == "1"
