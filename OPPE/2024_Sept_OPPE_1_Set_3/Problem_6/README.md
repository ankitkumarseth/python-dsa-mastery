# Word Filters

Given a list of words (case-insensitive), filter the words based on specific criteria and return the result as a list in the same order as the input. The criteria are as follows:

- `'continuous'`: words that end with "ing" (case-insensitive)
- `'vowel_rich'`: words that contain more than 5 vowels (not equal to 5)
- `'consonant_rich'`: words that contain more than 5 consonants (not equal to 5)
- `'sorted'`: words where the letters are sorted in ascending order

If any other criteria is given, return `None`.

*Note: You can use the string methods like `isalpha` and `lower` if needed.*

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition. You can define helper functions if needed, but the actual solution should be in the given function template.

### Example

For the list `["running", "aeiobcdioe", "acc", "xyz", "BOTbot" , "BboOTt" ,"jumpiNg", "SPINNING", "alphabetical"]`:

- **continuous** criteria will yield `["running", "jumpinNg", 'SPINNING']`
- **vowel_rich** criteria will yield `["aeiobcdioe"]`
- **consonant_rich** criteria will yield `["SPINNING", "alphabetical"]`
- **sorted** criteria will yield `["acc", "xyz", "BboOTt"]`
