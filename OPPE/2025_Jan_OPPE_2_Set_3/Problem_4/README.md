# Words with Consecutive Identical Letters

Write a function `words_with_consecutive_letters(words)` that takes a list of words and returns a list of words that contain at least one pair of consecutive identical letters (e.g., "hello", "apple"). The function should be case-insensitive.

The order of the words in the result should be same as they are present in the input.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples
- `words = ["hello", "apple", "ball", "test", "cat"]` -> `["hello", "apple", "ball"]`
  - Explanation: "hello" has 'll', "apple" has 'pp', "ball" has 'll'.
- `words = ["sky", "fly", "run", "jump"]` -> `[]`
  - Explanation: No words have consecutive identical letters.
