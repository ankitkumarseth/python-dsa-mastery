import ast
import inspect
import textwrap

def assert_no_loops_or_if(func):
    """
    Analyzes the Abstract Syntax Tree (AST) of the given function to ensure
    it does not contain any 'for' loops, 'while' loops, or 'if' statements.
    Raises an AssertionError if forbidden constructs are found.
    """
    source_lines, _ = inspect.getsourcelines(func)
    source = "".join(source_lines)
    source = textwrap.dedent(source)

    tree = ast.parse(source)

    for node in ast.walk(tree):
        if isinstance(node, ast.For):
            raise AssertionError(f"Function '{func.__name__}' is not allowed to use 'for' loops.")
        elif isinstance(node, ast.While):
            raise AssertionError(f"Function '{func.__name__}' is not allowed to use 'while' loops.")
        elif isinstance(node, ast.If):
            raise AssertionError(f"Function '{func.__name__}' is not allowed to use 'if' statements.")

def assert_no_for_loops_in_file(file_path):
    """
    Analyzes the AST of an entire file to ensure it does not contain any 'for' loops.
    Raises an AssertionError if 'for' loops are found.
    """
    with open(file_path, 'r') as f:
        source = f.read()

    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.For):
            raise AssertionError(f"File '{file_path}' is not allowed to use 'for' loops.")


def assert_no_while_loops_in_file(file_path):
    """
    Analyzes the AST of an entire file to ensure it does not contain any 'while' loops.
    Raises an AssertionError if 'while' loops are found.
    """
    with open(file_path, 'r') as f:
        source = f.read()

    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.While):
            raise AssertionError(f"File '{file_path}' is not allowed to use 'while' loops.")
