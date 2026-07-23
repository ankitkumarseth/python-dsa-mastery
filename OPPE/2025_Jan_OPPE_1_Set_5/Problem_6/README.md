# Key Stroke Analysis

Given a list of tuples representing key press events in the format `(key, press_time, release_time)`, where `press_time` and `release_time` are in milliseconds, implement the following functions.

- `average_hold_time(data: list, key: str) -> float`: Computes the average duration a specific key is held before release.
- `average_transition_time(data: list, key1: str, key2: str) -> float`: Computes the average time taken to transition between two specific keys.
- `get_typed_text(data: list) -> str`: Computes the final text considering the character keys and backspaces typed.
- `words_per_minute(data: list) -> float`: Computes the words per minute based on the total time taken for the key press events. Words can be separated by varying number of spaces. The total time is the duration between the first key press and the last key release.

The keys will one of be A to Z, SPACE and BACKSPACE.

Assume the key presses are sorted in the order in which they are typed and there is no overlap in key timings, that is only one key is pressed at a time.

**NOTE:** This is a function-type question. You don't have to take input or print the output, just have to complete the required function definitions.
