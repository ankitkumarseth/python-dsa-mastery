import os
import pytest

SOLUTION_FILE = os.path.join(os.path.dirname(__file__), 'solution.py')

import importlib.util
spec = importlib.util.spec_from_file_location("solution", SOLUTION_FILE)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_1():
    assert solution.markdown_to_html_image("![Cat](cat.jpg)") == '<img src="cat.jpg" alt="Cat">'

def test_2():
    assert solution.markdown_to_html_image("![Python Logo](python.png)") == '<img src="python.png" alt="Python Logo">'

def test_3():
    assert solution.markdown_to_html_image("![Funny Dog](doggo.jpeg)") == '<img src="doggo.jpeg" alt="Funny Dog">'

def test_4():
    assert solution.markdown_to_html_image("![](hello.jpg)") == '<img src="hello.jpg" alt="">'
