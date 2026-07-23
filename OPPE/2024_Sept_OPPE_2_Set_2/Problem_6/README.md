# Call Log Analysis

You are provided with a call log history represented as a list of dictionaries. Each dictionary contains the following keys:
- `name` (str): The name of the caller.
- `duration` (int): The duration of the call in seconds.

There will be multiple entries with the same name in the dataset. Implement a function `process_call_logs(call_logs, task)` where task is one of the following:

- `get_call_counts`: Returns a dictionary with caller names as keys and the count of their calls as values.
- `get_total_call_durations`: Returns a dictionary with caller names as keys and the total duration of their calls as values.
- `most_frequent_caller`: Returns the name of the caller with the highest number of calls. If there is a tie, the name with most call duration is returned.

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Example

```python
call_log = [
    {"name": "Alice", "duration": 300},
    {"name": "Bob", "duration": 200},
    {"name": "Alice", "duration": 100},
    {"name": "Bob", "duration": 400},
    {"name": "Charlie", "duration": 300}
]
```
- **get_call_counts** -> `{'Alice': 2, 'Bob': 2, 'Charlie': 1}`
- **get_total_call_durations** -> `{'Alice': 400, 'Bob': 600, 'Charlie': 300}`
- **most_frequent_caller** -> `'Bob'` *(Alice and Bob have the same number of calls but Bob has the most duration.)*
