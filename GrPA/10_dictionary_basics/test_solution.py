import pytest
from solution import dictionary_operations, increase_prices, dict_from_string, dict_to_string
from utils.code_inspectors import assert_no_loops_or_if

def test_dictionary_operations(capsys):
    # 1. AST Check
    assert_no_loops_or_if(dictionary_operations)

    # 2. Setup
    fruits = ["Apple", "Orange", "Grapes", "Banana", "Cherry"]
    fruit_prices = {
        "Orange": 4, "Grapes": 3,
        "Banana": 2, "Cherry": 5,
    }

    # 3. Execute
    dictionary_operations(fruit_prices, fruits)

    # 4. Check Final Dictionary State
    expected_dict = {'Apple': 3, 'Cherry': 5, 'Grapes': 5, 'Orange': 2}
    assert fruit_prices == expected_dict, "The final dictionary state is incorrect."

    # 5. Check Output Prints
    captured = capsys.readouterr()
    outputs = captured.out.strip().split('\n')

    assert len(outputs) == 3, "Expected exactly 3 print statements."
    assert outputs[0] == "5", f"Expected to print price of fruits[4] (5), but got {outputs[0]}"
    assert outputs[1] == "['Apple', 'Cherry', 'Grapes', 'Orange']", "Names list print is incorrect."
    assert outputs[2] == "[2, 3, 5, 5]", "Prices list print is incorrect."

def test_increase_prices():
    fruit_prices = {
        "Orange": 4, "Grapes": 3,
        "Banana": 2, "Cherry": 5,
    }

    increase_prices(fruit_prices)

    expected_dict = {
        'Orange': 4.8, 'Grapes': 3.6,
        'Banana': 2.4, 'Cherry': 6.0
    }
    assert fruit_prices == expected_dict, "Prices were not increased by exactly 20% and rounded correctly."

def test_dict_from_string():
    input_str = """Apple,2
Banana,3
Orange,4
Grapes,3
Papaya,5"""

    result = dict_from_string(input_str, str, int)
    expected = {
        'Apple': 2,
        'Banana': 3,
        'Orange': 4,
        'Grapes': 3,
        'Papaya': 5
    }

    assert result == expected, "String was not converted to dictionary correctly."

def test_dict_to_string():
    # 1. AST Check
    assert_no_loops_or_if(dict_to_string)

    # 2. Execution
    input_dict = {
        'Apple': 2,
        'Banana': 3,
        'Orange': 4,
        'Grapes': 3,
        'Papaya': 5
    }

    expected_str = "Apple,2\nBanana,3\nOrange,4\nGrapes,3\nPapaya,5"
    result = dict_to_string(input_dict)

    # Strip any trailing newlines from result for safety
    assert result.strip() == expected_str.strip(), "Dictionary was not converted back to string correctly."
