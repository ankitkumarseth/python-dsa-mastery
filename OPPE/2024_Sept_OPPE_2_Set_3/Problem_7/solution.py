import sys

def solve():
    # Write your code to read the file and print the result.
    # use the variable filename for the name of the file.
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            content = f.read()
    else:
        content = sys.stdin.read()
        
    # Write your logic here
    ...

if __name__ == '__main__':
    solve()
