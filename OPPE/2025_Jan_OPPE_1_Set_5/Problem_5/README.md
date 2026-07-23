# Score Objective Questions

Given the type of question with the correct answer and the student's answer separated by space over multiple lines, find the total marks and number of correct answers, assuming each question has three marks for a correct answer and a `choice` type question also has a negative one marks for an incorrect answer. `range` type question has no negative marks.

The range in the `range` type question is given in the format `{low}..{high}`.

- The `choice` type answer is correct if both the answer given and the student's answer are same.
- The `range` type answer is correct if `low <= student_answer <= high`.

**NOTE:** This is an I/O type question, you need to write the whole code for taking input and printing the output.

### Input Format
The first line contains an integer `n` representing the number of questions.
The next `n` lines each contain the question type (`choice` or `range`), the correct answer (or range), and the student's answer.

### Output Format
A single integer representing the total score.
An integer representing the total number of correct answers.

### Example

**Input:**
```
4
choice a b
range 1..4 3
choice b b
range 1.1..4.5 5
```
**Output:**
```
5
2
```
