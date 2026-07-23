import os, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_transactions(capsys):
    input_data1 = "2\n150\n-10 10 -10 5\n20 -20 30 -10\n"
    solution.solve(input_data1)
    assert capsys.readouterr().out == "140,150,145\n145,175,165\n"

    input_data2 = "3\n100\n-20 30 -50\n10 -20 30\n-10 40 -30\n"
    solution.solve(input_data2)
    assert capsys.readouterr().out == "60,110,60\n50,80,80\n70,110,80\n"
