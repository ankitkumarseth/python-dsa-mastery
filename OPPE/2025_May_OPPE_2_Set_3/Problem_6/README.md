# Book Reading List Data Analysis

You are given a list of dictionaries, each representing a book in a reading list.
Every dictionary contains the following keys:
- `book_id` (str) a unique identifier for the book
- `pages` (int) the number of pages of the book
- `rating` (float) the rating of the book (0-5)

Implement a function `book_analysis(data, request)` that performs the operation specified by `request` on the list `data`.

Supported requests:
- `average_rating` - Return the average rating of all books, rounded to two decimal places.
- `average_pages` - Return the average number of pages of all books, rounded to two decimal places.
- `longest_book` - Return the `book_id` of the book with the maximum number of pages. If several books share the same maximum page count, return the one among them with the highest rating.
- `above_average_books` - Return a set of `book_ids` of books that satisfy both conditions:
  - rating strictly greater than the average rating of all books, and
  - pages strictly greater than the average number of pages.

NOTE: This is a function type question, you don't have to take input or print the output, you just have to complete the required function definition.

### Example
```python
data = [
    {"book_id": "X1", "pages": 540, "rating": 4.9},
    {"book_id": "X2", "pages": 96,  "rating": 4.6},
    {"book_id": "X3", "pages": 1225,"rating": 4.4},
    {"book_id": "X4", "pages": 328, "rating": 4.2},
    {"book_id": "X5", "pages": 180, "rating": 3.9},
    {"book_id": "X6", "pages": 1225,"rating": 4.3},
]
```
- `book_analysis(data, "average_rating")` -> `4.38`
- `book_analysis(data, "average_pages")` -> `599.0`
- `book_analysis(data, "longest_book")` -> `'X3'`
- `book_analysis(data, "above_average_books")` -> `{'X3'}`
