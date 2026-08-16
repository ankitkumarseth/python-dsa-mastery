# Total Size of Image Files

Given a file containing file sizes and file names separated by a comma, find the total size of image files with extensions `.jpg`, `.jpeg`, `.png`, and `.gif` (case insensitive).

### Assumptions
- The file is in the standard format where each line has a file size followed by a file name.
- The file size is in bytes.
- The file name is in the format `filename.extension`.

### Examples

**Input File (`test_input.txt`):**
```text
2000,file1.jpg
890,file2.txt
30500,file3.JPEG
12000,file4.png
40000,file5.gif
490,file6.docx
```

**Output:**
```text
84500
```
**Explanation:**
The total size of image files, which is 2000 + 30500 + 12000 + 40000 = 84500
