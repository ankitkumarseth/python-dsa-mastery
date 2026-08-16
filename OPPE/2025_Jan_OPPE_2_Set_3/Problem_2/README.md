# Absolute Time Difference Between Two Times

Write a function `absolute_time_difference` that takes two time strings in the format `HH:MM` as input and returns the absolute time difference between them in the same format.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

For example, given the times `14:30` and `06:45`, the function should return `07:45`, because this is the absolute time difference between the two input times.

HINT: You might want to use formatted string with `{val:02}` for padding time with leading 0 in case of single digit.

### Examples
- `absolute_time_difference('14:30', '06:45')` -> `'07:45'`
- `absolute_time_difference('06:45', '14:30')` -> `'07:45'`
- `absolute_time_difference('02:30', '03:10')` -> `'00:40'`
- `absolute_time_difference('23:59', '00:00')` -> `'23:59'`
