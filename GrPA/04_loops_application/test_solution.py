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

# --- factors ---


def test_factors_tc1():
    assert run_script("factors\n28\n") == "1\n2\n4\n7\n14\n28"

def test_factors_edge():
    # Prime number 13 should have factors 1 and 13
    assert run_script("factors\n13\n") == "1\n13"

# --- find_min ---


def test_find_min_tc2():
    assert run_script("find_min\n5\n10\n20\n5\n25\n15\n") == "5"

def test_find_min_edge():
    # Negative numbers and negative answer
    assert run_script("find_min\n3\n-5\n-1\n-10\n") == "-10"

# --- prime_check ---


def test_prime_check_tc3():
    assert run_script("prime_check\n17\n") == "True"

def test_prime_check_edge1():
    assert run_script("prime_check\n1\n") == "False"

def test_prime_check_edge2():
    assert run_script("prime_check\n9\n") == "False"

def test_prime_check_edge3():
    assert run_script("prime_check\n2\n") == "True"

# --- is_sorted ---


def test_is_sorted_tc4():
    assert run_script("is_sorted\nabcdefg\n") == "True"

def test_is_sorted_tc5():
    assert run_script("is_sorted\nzyx\n") == "False"

def test_is_sorted_edge():
    assert run_script("is_sorted\naabbcc\n") == "True"

# --- any_true ---


def test_any_true_tc6():
    assert run_script("any_true\n4\n10\n15\n20\n25\n") == "True"

def test_any_true_tc7():
    assert run_script("any_true\n3\n10\n20\n25\n") == "False"

# --- manhattan ---


def test_manhattan_tc8():
    assert run_script("manhattan\nUP\nUP\nLEFT\nDOWN\nRIGHT\nRIGHT\nSTOP\n") == "2"

def test_manhattan_edge():
    # Down 3, Left 4 -> dist = 7
    assert run_script("manhattan\nDOWN\nDOWN\nDOWN\nLEFT\nLEFT\nLEFT\nLEFT\nSTOP\n") == "7"
