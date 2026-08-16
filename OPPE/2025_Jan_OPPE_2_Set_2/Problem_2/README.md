# Shuffle a Three Word Sentence

Write a function `shuffle_sentence(sentence, order)` that takes a string `sentence` containing three words separated by spaces and a tuple `order` specifying the shuffling order.

The function should return a string with the words of the sentence shuffled according to the specified order.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Examples
- `sentence = "apple banana orange", order = (0, 2, 1)` -> `"apple orange banana"`
  - Explanation: 0 - apple, 2 - orange, 1 - banana
- `sentence = "cat dog mouse", order = (2, 1, 0)` -> `"mouse dog cat"`
  - Explanation: 2 - mouse, 1 - dog, 0 - cat
