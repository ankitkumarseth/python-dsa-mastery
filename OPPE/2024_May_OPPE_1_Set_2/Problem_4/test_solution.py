import os, importlib.util
SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_antakshari(capsys):
    input_data = "3\none,two,order,real,long,tight,tree,cool,lot,trouble\none,two,three,four,five\nfive,six,seven,nine,eight,two,one,eleven,six,seven\n"
    solution.solve(input_data)
    out = capsys.readouterr().out
    assert out == "4\n1\n6\n"
