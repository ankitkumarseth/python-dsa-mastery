import subprocess
import os
import pytest
from utils.code_inspectors import assert_no_for_loops_in_file

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def run_script(input_text):
    result = subprocess.run(
        ["python3", SOLUTION_FILE],
        input=input_text,
        text=True,
        capture_output=True
    )
    # Return stripped output but handle empty case securely
    return result.stdout.strip()

def test_ast_no_for_loops():
    # Enforce that the student did not use any for loops anywhere in the file
    assert_no_for_loops_in_file(SOLUTION_FILE)

# --- Accumulation ---


def test_sum_until_0_tc1():
    input_text = "sum_until_0\n5\n3\n2\n0\n"
    assert run_script(input_text) == "10"

def test_sum_until_0_tc2():
    input_text = "sum_until_0\n10\n-5\n5\n0\n"
    assert run_script(input_text) == "10"

def test_total_price_tc3():
    input_text = "total_price\n2 50\n1 100\n3 30\nEND\n"
    assert run_script(input_text) == "290"

def test_total_price_tc4():
    input_text = "total_price\n5 10\n2 20\nEND\n"
    assert run_script(input_text) == "90"

# --- Filtering ---


def test_only_ed_or_ing_tc5():
    input_text = "only_ed_or_ing\nReading\ncompleted\nrunning\nstart\nEND\nSTOP\n"
    expected = "Reading\ncompleted\nrunning"
    assert run_script(input_text) == expected

def test_only_ed_or_ing_tc6():
    input_text = "only_ed_or_ing\nopened\nclose\nstopped\nmove\ningested\nSTOP\n"
    expected = "opened\nstopped\ningested"
    assert run_script(input_text) == expected

def test_reverse_sum_palindrome_tc7():
    input_text = "reverse_sum_palindrome\n56\n99\n32\n-1\n"
    expected = "56\n32"
    assert run_script(input_text) == expected

def test_reverse_sum_palindrome_tc8():
    input_text = "reverse_sum_palindrome\n12\n19\n23\n34\n87\n-1\n"
    expected = "12\n23\n34"
    assert run_script(input_text) == expected

# --- Mapping ---


def test_double_string_tc9():
    input_text = "double_string\nhello\nworld\n\n"
    expected = "hellohello\nworldworld"
    assert run_script(input_text) == expected

def test_double_string_tc10():
    input_text = "double_string\nfoo\nbar\nbaz\n\n"
    expected = "foofoo\nbarbar\nbazbaz"
    assert run_script(input_text) == expected

def test_odd_char_tc11():
    input_text = "odd_char\nHello\nWORLD.\n"
    expected = "Hlo WRD"
    assert run_script(input_text) == expected

def test_odd_char_tc12():
    input_text = "odd_char\nThis\nis\na \nsample\nsentence.\n"
    expected = "Ti i a sml snec."
    assert run_script(input_text) == expected

# --- Filter and Map ---


def test_only_even_squares_tc13():
    input_text = "only_even_squares\n3\n4\n5\nNAN\n"
    expected = "16"
    assert run_script(input_text) == expected

def test_only_even_squares_tc14():
    input_text = "only_even_squares\n2\n7\n8\nNAN\n"
    expected = "4\n64"
    assert run_script(input_text) == expected

# --- Filter and Accumulate ---


def test_only_odd_lines_tc15():
    input_text = "only_odd_lines\none\ntwo\nthree\nfour\nEND\n"
    expected = "three\none"
    assert run_script(input_text) == expected

def test_only_odd_lines_tc16():
    input_text = "only_odd_lines\nline1\nline2\nline3\nEND\n"
    expected = "line3\nline1"
    assert run_script(input_text) == expected
