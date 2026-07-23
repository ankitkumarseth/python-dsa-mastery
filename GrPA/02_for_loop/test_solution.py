import subprocess
import os
import pytest
from utils.code_inspectors import assert_no_while_loops_in_file

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def run_script(input_text):
    result = subprocess.run(
        ["python3", SOLUTION_FILE],
        input=input_text,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()

def test_ast_no_while_loops():
    assert_no_while_loops_in_file(SOLUTION_FILE)

# --- Part 1 ---


def test_factorial_tc1():
    assert run_script("factorial\n5\n") == "120"

def test_factorial_tc2():
    assert run_script("factorial\n7\n") == "5040"

def test_factorial_edge_zero():
    # 0! is 1
    assert run_script("factorial\n0\n") == "1"

def test_even_numbers_tc3():
    assert run_script("even_numbers\n10\n") == "0\n2\n4\n6\n8\n10"

def test_even_numbers_tc4():
    assert run_script("even_numbers\n5\n") == "0\n2\n4"

def test_power_sequence_tc5():
    assert run_script("power_sequence\n5\n") == "1\n2\n4\n8\n16"

def test_power_sequence_tc6():
    assert run_script("power_sequence\n3\n") == "1\n2\n4"

def test_power_sequence_edge_zero():
    # Sequence of 0 terms should print nothing
    assert run_script("power_sequence\n0\n") == ""

# --- Part 2 ---


def test_sum_not_divisible_tc7():
    assert run_script("sum_not_divisible\n15\n") == "66"

def test_sum_not_divisible_tc8():
    assert run_script("sum_not_divisible\n10\n") == "28"

def test_from_k_tc9():
    assert run_script("from_k\n5\n99\n") == "78\n38\n18\n77\n37"

def test_from_k_tc10():
    assert run_script("from_k\n3\n55\n") == "74\n34\n14"

# --- Part 3 ---


def test_string_iter_tc11():
    assert run_script("string_iter\n1234\n") == "1\n2\n6\n12"

def test_string_iter_tc12():
    assert run_script("string_iter\n567\n") == "5\n30\n42"

def test_list_iter_tc13():
    input_text = "list_iter\n[1, 2.0, \"three\", True]\n"
    expected = "1 - type: <class 'int'>\n2.0 - type: <class 'float'>\nthree - type: <class 'str'>\nTrue - type: <class 'bool'>"
    assert run_script(input_text) == expected

def test_list_iter_tc14():
    input_text = "list_iter\n[\"apple\", ... , [1,2], None]\n"
    expected = "apple - type: <class 'str'>\nEllipsis - type: <class 'ellipsis'>\n[1, 2] - type: <class 'list'>\nNone - type: <class 'NoneType'>"
    assert run_script(input_text) == expected

def test_list_iter_edge_empty():
    assert run_script("list_iter\n[]\n") == ""
