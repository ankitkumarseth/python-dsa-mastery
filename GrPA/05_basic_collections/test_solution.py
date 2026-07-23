import os
import pytest
from utils.code_inspectors import assert_no_for_loops_in_file

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

def get_student_code():
    with open(SOLUTION_FILE, 'r') as f:
        content = f.read()
    return content.split("# --- STUDENT CODE BEGINS ---")[1]

def run_with_globals(**injected_globals):
    code = get_student_code()

    # Default globals that the script expects to be defined
    local_ns = {
        "int_iterable": range(1, 10, 3),
        "string_iterable": ["Apple", "Orange", "Banana"],
        "some_value": 4,
        "some_collection": [1, 2, 3],
        "some_iterable": (1, 2, 3),
        "another_iterable": {"apple", "banana", "cherry"},
        "yet_another_iterable": range(1, 10)
    }
    # Update with test-specific overrides
    local_ns.update(injected_globals)

    exec(code, {}, local_ns)
    return local_ns

def test_ast_no_for_loops():
    assert_no_for_loops_in_file(SOLUTION_FILE)

def test_empty_types():
    ns = run_with_globals()
    assert type(ns.get("empty_list")).__name__ == "list"
    assert type(ns.get("empty_set")).__name__ == "set"
    assert type(ns.get("empty_tuple")).__name__ == "tuple"
    assert len(ns.get("empty_list")) == 0
    assert len(ns.get("empty_set")) == 0
    assert len(ns.get("empty_tuple")) == 0

def test_singleton_types():
    ns = run_with_globals()
    assert type(ns.get("singleton_list")).__name__ == "list"
    assert type(ns.get("singleton_set")).__name__ == "set"
    assert type(ns.get("singleton_tuple")).__name__ == "tuple"
    assert len(ns.get("singleton_list")) == 1
    assert len(ns.get("singleton_set")) == 1
    assert len(ns.get("singleton_tuple")) == 1

def test_truthiness():
    ns = run_with_globals()
    assert type(ns.get("a_falsy_list")).__name__ == "list"
    assert bool(ns.get("a_falsy_list")) == False
    assert type(ns.get("a_falsy_set")).__name__ == "set"
    assert bool(ns.get("a_falsy_set")) == False
    assert type(ns.get("a_truthy_tuple")).__name__ == "tuple"
    assert bool(ns.get("a_truthy_tuple")) == True

def test_int_iterable_basics():
    # Min/Max test
    ns1 = run_with_globals(int_iterable=[4,2,4,6,7,3,-2,3])
    assert ns1["int_iterable_min"] == -2

    ns2 = run_with_globals(int_iterable={4,2,4,6,7,3,-2,3})
    assert ns2["int_iterable_max"] == 7

    # Sum/Len test
    ns3 = run_with_globals(int_iterable=range(10))
    assert ns3["int_iterable_sum"] == 45

    ns4 = run_with_globals(int_iterable=range(20))
    assert ns4["int_iterable_len"] == 20

def test_int_iterable_sorting():
    ns1 = run_with_globals(int_iterable={4,2,4,6,7,3,-2,3})
    assert ns1["int_iterable_sorted"] == [-2, 2, 3, 4, 6, 7]

    ns2 = run_with_globals(int_iterable=(4,2,4,6,7,3,-2,3))
    assert ns2["int_iterable_sorted_desc"] == [7, 6, 4, 4, 3, 3, 2, -2]

def test_int_iterable_reversed():
    ns1 = run_with_globals(int_iterable=[4,2,4,6,7,3,-2,3])
    assert ns1["int_iterable_reversed"] == [3, -2, 3, 7, 6, 4, 2, 4]

    ns2 = run_with_globals(int_iterable={4,2,4,6,7,3,-2,3})
    assert ns2["int_iterable_reversed"] == [7, 6, 4, 3, 2, -2]

def test_third_last_element():
    ns1 = run_with_globals(some_collection=list(range(10)))
    assert ns1["third_last_element"] == 7

    ns2 = run_with_globals(some_collection=set(range(10)))
    assert ns2["third_last_element"] is None

def test_odd_index_elements():
    ns1 = run_with_globals(some_collection=tuple(range(10)))
    assert ns1["odd_index_elements"] == (1, 3, 5, 7, 9)

    ns2 = run_with_globals(some_collection=set(range(10)))
    assert ns2["odd_index_elements"] is None

def test_is_some_value_in_collection():
    ns1 = run_with_globals(some_collection=set(range(5,21,5)), some_value=20)
    assert ns1["is_some_value_in_some_collection"] is True

    ns2 = run_with_globals(some_collection=list(range(5,21,5)), some_value=19)
    assert ns2["is_some_value_in_some_collection"] is False

def test_is_some_value_in_even_indices():
    ns1 = run_with_globals(some_collection=list("Hello"), some_value="o")
    assert ns1["is_some_value_in_even_indices"] is True

    ns2 = run_with_globals(some_collection=list("Hello"), some_value="lo")
    assert ns2["is_some_value_in_even_indices"] is False

    ns3 = run_with_globals(some_collection="Hello", some_value="e")
    assert ns3["is_some_value_in_even_indices"] is False

def test_all_iterables():
    ns1 = run_with_globals(
        some_iterable=[1,2,4],
        another_iterable=range(4),
        yet_another_iterable=(1,2,3,4,5)
    )
    assert ns1["all_iterables"] == [1, 2, 4, 0, 1, 2, 3, 1, 2, 3, 4, 5]

def test_all_concat():
    ns1 = run_with_globals(string_iterable=["Banana","Cherry","Apple"])
    assert ns1["all_concat"] == "Banana-Cherry-Apple"

    ns2 = run_with_globals(string_iterable={"Banana", "Mango", "Cherry","Apple"})
    assert ns2["all_concat"] == "Apple-Banana-Cherry-Mango"
