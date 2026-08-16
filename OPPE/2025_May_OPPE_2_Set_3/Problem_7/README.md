# Column Totals in a Markdown Table (Numeric Columns Only)

Read the contents of a file containing a markdown table with integer values and print the column sums.

### Markdown table format
- First line contains the headers surrounded and separated by `|` character.
- Second line is header separator containing `|` and `-` and has no data.
- Every following line is a data row with values surrounded and separated by `|` character.
- Spaces may appear around the pipes and around the cell contents.
- All columns contain integer values (positive, negative or zero).

### Output format
One column sum per line, in the format:
`<column_name>: <total>`

The order of the output must follow the order of the columns in the header.

Note: This is a file-in-stdout type problem—the whole input should be written to a temporary file first, and the solution must read from that file.

### Examples

**Input:**
```text
| Score |
|------|
| 10 |
| 15 |
| 20 |
```
**Output:**
```text
Score: 45
```

**Input:**
```text
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
```
**Output:**
```text
A: 12
B: 15
C: 18
```
