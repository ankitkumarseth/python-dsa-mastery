import os, pytest, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_rle(capsys):
    input_data = "4\n444555\n666666\n77778888\n234567\n"
    solution.solve(input_data)
    captured = capsys.readouterr()
    expected = "3 4 3 5\n6 6\n4 7 4 8\n1 2 1 3 1 4 1 5 1 6 1 7\n"
    assert captured.out == expected
