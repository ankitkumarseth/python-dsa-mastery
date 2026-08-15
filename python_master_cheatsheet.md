# The Ultimate Python Cheatsheet (For Java Developers)

Welcome to your central hub for Python mastery. If you are ever stuck on "how do I do X in Python that I used to do in Java?", this is your reference.

---

## 1. The Absolute Basics

### Variables & Typing
Python is dynamically typed. You don't declare types, but you *can* use type hints for readability (highly recommended for production code).

```python
name: str = "Alice"
age: int = 30
is_active: bool = True  # Note: True/False are capitalized!
nothing: None = None    # Python's version of 'null'

# OPPE Gotcha: Simultaneous Swapping
a, b = b, a # Swaps inherently without a temp variable!
```

### Initializing Min/Max (DSA Pro-Tip)
In Java you use `Integer.MAX_VALUE`. In Python, you use infinity.
```python
max_val = float('inf')
min_val = float('-inf')
```

### Exceptions
Python uses `try` / `except` (instead of `try` / `catch`).
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught error: {e}")
finally:
    print("Always runs")
```

---

## 2. Strings (The Missing Link)

Strings are immutable (just like in Java). They are ubiquitous in Python DSA problems.

```python
s = "  hello world  "
s = s.strip()            # "hello world" (Java's trim())
parts = s.split(" ")     # ["hello", "world"]
joined = "-".join(parts) # "hello-world"
replaced = s.replace("world", "Python") # "hello Python"
```

**OPPE Gotcha (Immutability)**: Trying to modify a character by index (`s[0] = 'x'`) throws a TypeError. You MUST re-slice: `s = 'x' + s[1:]`.

**OPPE Gotcha (Splitting)**: `"".split("-")` returns `[""]` (a list containing one empty string), but `"a".split("-")` returns `["a"]`. However, `"".split()` (with no arguments) handles whitespace properly and returns `[]`.
**OPPE Gotcha (`splitlines()` vs `split('\n')`)**: Always use `.splitlines()` when parsing multi-line text! `split('\n')` leaves an empty string `""` at the end of your list if the text ends with a newline, and fails to handle Windows `\r\n` carriage returns properly. `splitlines()` safely handles both.

**OPPE Gotcha (Alignment / Patterns)**: For drawing ASCII patterns, do not use nested loops. Use string multiplication (`"*" * 5`) and built-in alignment: `"x".center(5)`, `s.rjust(5)`, or `s.zfill(3)`.

### Slicing `[start:stop:step]`
You can slice arrays and strings effortlessly.
```python
s = "Mastercard"
print(s[0:6])   # 'Master' (Index 0 to 5)
print(s[-4:])   # 'card' (Last 4 characters)
print(s[::-1])  # 'dracretsaM' (Reverses the string!)
```

### Advanced Slicing Tricks
You can use slicing creatively to avoid writing deletion logic entirely, or to manipulate specific patterns.
```python
# 1. Slicing for Deletion: Just keep what you need!
# E.g., to "delete" even indices, just keep the odd indices:
odd_indices_only = items[1::2]

# 2. Extended Slice Assignment
# The strictly enforced rule: the replacing iterable MUST match the exact length of the slice you are replacing!
items[::2] = [None] * len(items[::2])
```

---

## 3. Core Data Structures (The DSA Toolbelt)

### Lists (Java `ArrayList`)
Python lists are highly versatile. Here are the core methods you need to know for DSA:

```python
arr = [10, 20, 30]

# 1. Adding Elements
arr.append(40)          # Adds 40 to the end: O(1)
arr.insert(1, 15)       # Inserts 15 at index 1 (shifts rest right): O(N)
arr.extend([50, 60])    # Appends multiple elements to the end: O(K)
```

**OPPE Gotcha**: Python lists can seamlessly mix types, like `[1, -2, None, 4]`. Operations require checking identity (`if x is not None:`) before performing math comparisons to avoid a `TypeError`.

**Finding and Counting Elements**
```python
count_of_twos = arr.count(2)  # Counts exact occurrences without a loop!
first_index = arr.index(20)   # Returns index of first occurrence of 20

# Pro-Tip: The Boolean Counting Trick
# If you need to count occurrences of a *complex condition*, use sum() with a generator!
# True evaluates to 1, False evaluates to 0.
even_count = sum(x % 2 == 0 for x in arr) 
```

**Finding the Last Index in a List (The Reverse Trick)**
Unlike strings which have `.rindex()`, Python lists and tuples only have `.index()`, which returns the *first* matching index.
To find the *last* index of an element, you can reverse the list, find the first index in the reversed list, and subtract it from the total length:
```python
items = [1, 2, 3, 1, 5, 6]
elem = 1

# 1. Reverses the list: items[::-1]
# 2. Finds the index of the element from the "right" side
# 3. Math to translate it back to the original left-side index
last_index = len(items) - items[::-1].index(elem) - 1 # Returns 3
```

**Deletion Nuances (`remove` vs `del` vs `discard` vs `pop`)**

**OPPE Gotcha (Shifting Trap)**: Deleting elements at two specific indices in-place requires accounting for the list length changing! Delete the larger index first: `arr.pop(max(i1, i2))` then `arr.pop(min(i1, i2))`.

When manipulating collections, be highly specific about *how* you want to remove an item:
*   **`list.remove(value)` / `set.remove(value)`**: Removes the *first occurrence* of a specific value. Throws an error if the value doesn't exist.
*   **`set.discard(value)`**: Removes a value from a set *safely*. Does absolutely nothing if the value doesn't exist. (Lists do not have this).
*   **`del list[index]` / `del dict[key]`**: Standard Python keyword to remove an element by its exact index or key. Throws an error if the index/key doesn't exist. Does *not* return the deleted item.
*   **`list.pop(index)` / `dict.pop(key)`**: Deletes the element by its exact index or key **and returns it**. If you don't need the returned value, `del` is slightly faster and more semantic.

### Tuples (Immutable Lists)
Tuples are just like lists, but they are **immutable** (cannot be changed after creation). This makes them perfect for storing coordinate pairs `(x, y)` or using them as keys in a Dictionary!

```python
# 1. Creation
point = (10, 20)
single = (5,)               # MUST have a comma for a single-element tuple!

# 2. Unpacking (Massively useful in DSA)
x, y = point                # x = 10, y = 20

# 3. Operations (No mutation allowed)
# point[0] = 15             # ERROR! Tuples are immutable.
print(point[0])             # 10 (Access is O(1))
```
**OPPE Gotcha**: Tuples don't support element-wise arithmetic. `(1, 2) + (3, 4)` is `(1, 2, 3, 4)`, not `(4, 6)`. You have to do math on individual indexes manually `(a[0]+b[0], a[1]+b[1])`.
**OPPE Gotcha**: Tuple multiplication repeats elements! `(0,) * 3` gives `(0, 0, 0)`.

### Dictionaries (Java `HashMap`)
Dictionaries are Python's Hash Maps. They store key-value pairs and offer $O(1)$ lookups.

```python
map = {"Alice": 25, "Bob": 30}

# 1. Adding / Updating
map["Charlie"] = 35         # Put: O(1)
map.update({"Dave": 40})    # Bulk update: O(K)

# 2. Retrieving
age = map["Alice"]          # Unsafe retrieval (throws KeyError if missing)
age = map.get("Dave", 0)    # Safe Retrieval (Returns default 0 if not found)

# 3. Removing
del map["Bob"]              # Deletes key (throws KeyError if missing)
val = map.pop("Alice")      # Removes key AND returns its value
map.pop("Eve", None)        # Safe pop (returns None instead of throwing KeyError)

# 4. Iteration
keys = map.keys()           # View of keys
vals = map.values()         # View of values
for key, val in map.items():# Iterate both!
    print(f"{key} is {val}")

# Getting concrete Lists from dictionary views
list_of_tuples = list(map.items()) # Converts dict into a solid list of tuples!
```

**OPPE Gotcha**: You **cannot modify a dict while iterating over it**. If you need to delete keys in a loop, copy them to a list first!
```python
for k in list(d.keys()):
    if d[k] < 0:
        del d[k]
```

### Sets (Java `HashSet`)
Sets store unique elements and offer $O(1)$ lookups. They support powerful mathematical operations.

```python
seen = set([1, 2, 3])

# 1. Adding / Checking
seen.add(4)                 # Add element: O(1)
print(2 in seen)            # Check existence: True: O(1)

# 2. Set Operations (Math logic)
setA = {1, 2, 3}
setB = {3, 4, 5}
print(setA & setB)          # Intersection: {3}
print(setA | setB)          # Union: {1, 2, 3, 4, 5}
print(setA - setB)          # Difference: {1, 2}
print(setA ^ setB)          # Symmetric Diff (In A or B, but not both): {1, 2, 4, 5}

setA.difference_update(setB)# In-place Difference (Mutates setA to {1, 2})
```

**OPPE Gotcha (Order-Preserving Uniqueness)**: Generating unique lists relies on `set(lst)`. But sets destroy the original ordering! To remove duplicates *while preserving order*, use a dictionary (which maintains insertion order): `list(dict.fromkeys(lst))`.

### Queues / Deques (Java `LinkedList`)
If you need a Queue for BFS, **always use `collections.deque`**. 
```python
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)       # Enqueue to tail: O(1)
queue.appendleft(0)   # Enqueue to head: O(1)
queue.popleft()       # Dequeue from head: O(1)
queue.pop()           # Dequeue from tail: O(1)
```

### Heaps / Priority Queues (Java `PriorityQueue`)
Python's `heapq` is a **Min-Heap** by default. It transforms a normal list into a heap in-place.

```python
import heapq

# 1. Standard Min-Heap (Smallest value treated first)
min_heap = []
heapq.heappush(min_heap, 50)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 99)
smallest = heapq.heappop(min_heap)  # Returns 10

# 2. Max-Heap Trick (Largest value treated first)
# Multiply by -1 before pushing, and -1 again after popping
max_heap = []
heapq.heappush(max_heap, 50 * -1)
heapq.heappush(max_heap, 10 * -1)
heapq.heappush(max_heap, 99 * -1)
largest = heapq.heappop(max_heap) * -1  # Returns 99

# 3. Heapify an existing array: O(N) time!
arr = [9, 3, 2, 7]
heapq.heapify(arr) # Mutates arr into a valid heap in-place
```

### Advanced Collections (The DSA Secret Weapons)
If you are doing frequency counts or grouping elements, **do not** use a normal dictionary. Use these imports from `collections` to save yourself from writing boilerplate `if key in map:` logic.

**1. `Counter` (Frequency Counting)**
```python
from collections import Counter

# Instantly count frequencies of an array or string
counts = Counter([1, 1, 2, 3, 3, 3]) 
print(counts[3])       # Returns 3
print(counts[99])      # Returns 0 (No KeyError!)
print(counts.most_common(1)) # Returns [(3, 3)]

# OPPE Pro-Tip: Finding the most frequent element in O(N) time
# .most_common(1) returns a list with one tuple -> e.g. [('a', 5)]
# [0] grabs the first tuple -> ('a', 5)
# [0] grabs the first item in the tuple (the element itself) -> 'a'
mode = Counter(['a', 'a', 'b']).most_common(1)[0][0]
```

**2. `defaultdict` (Grouping / Graph Adjacency Lists)**
```python
from collections import defaultdict

# Example: Building an adjacency list for a Graph
graph = defaultdict(list)
graph["node_A"].append("node_B") # No need to check if "node_A" exists!

# Example: Grouping by a default int (0)
scores = defaultdict(int)
scores["Alice"] += 10
```

### Common Built-in Utilities
*   `max(arr)`, `min(arr)`, `sum(arr)`: Instantly compute aggregates.
*   `any(condition for x in arr)`: Returns `True` if *at least one* element matches. Pass a lazy generator expression `(x for x in arr)` to ensure it stops evaluating exactly when it hits `True`, giving you optimal $O(N)$ early-exit performance.
*   `all(condition for x in arr)`: Returns `True` if *every* element matches.

---

## 4. Iteration & Pythonic Sugar

### The Power of `enumerate` and `zip` (Iterables of Tuples)
Never use `for i in range(len(arr))` if you also need the value! `enumerate` and `zip` are your best friends, but it is critical to understand that **they return Iterables of Tuples**.

```python
names = ["Alice", "Bob"]
scores = [100, 95]

# enumerate(["Alice", "Bob"]) yields: (0, "Alice"), (1, "Bob")
# zip(names, scores) yields: ("Alice", 100), ("Bob", 95)

# Pro-Tip: The Adjacent Comparison Trick
# You can use zip on a list and its own slice to iterate over adjacent pairs without tracking indices!
# zip(arr, arr[1:]) yields: (arr[0], arr[1]), (arr[1], arr[2]), ...
```

**1. Tuple Unpacking (For Loops & Comprehensions)**
Because they yield tuples, you can elegantly unpack them directly in your loop variables!
```python
for i, name in enumerate(names):
    print(f"Index {i} is {name}")

result = {key: val for key, val in zip(names, scores)}
```

**2. Tuple Indexing (Lambda Maps & Filters)**
If you pass them into `map()` or `filter()`, a lambda function only takes a *single* argument. That argument becomes the entire Tuple! You must access the keys/values via indices `x[0]` and `x[1]`.
```python
# x is the tuple (0, "Alice")
# x[0] is the index, x[1] is the value
mapped = list(map(lambda x: x[1].upper(), enumerate(names))) 
```

**3. Casting to concrete Lists**
If you want to access indexes directly or print the entire output, you can cast the iterators to solid lists:
```python
list_of_tuples = list(enumerate(names)) # [(0, 'Alice'), (1, 'Bob')]
```

### The `for...else` Loop
Executes the `else` block **only** if the loop finishes *naturally* without hitting a `break`. This completely eliminates the need for boolean flags (like `is_prime = True`).
```python
for i in range(2, n):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime!") # Only runs if the loop never broke
```

### The Walrus Operator (`:=`)
Assigns a variable and evaluates it in a single line. Extremely Pythonic for while loops and conditionals.
```python
# Instead of:
# user_input = input()
# while user_input != "STOP":
#     ...
#     user_input = input()

# Do this:
while (user_input := input()) != "STOP":
    print(f"Processing {user_input}")
```

### Pattern Matching (`match-case`)
Use Python 3.10+ `match` as an elegant, clean alternative to long `if/elif` directional chains.
```python
match direction:
    case "RIGHT": x += 1
    case "LEFT":  x -= 1
    case "UP":    y += 1
    case "DOWN":  y -= 1
    case _:       print("Unknown direction") # Default case
```

---

## 5. Comprehensions & Generators

### List/Set/Dict Comprehensions
Transform data in one line.
```python
nums = [1, 2, 3, 4]
squares = [n * n for n in nums if n % 2 == 0] # [4, 16]
indexed = {i: name for i, name in enumerate(names)}
```

### Set Comprehensions
Just like you can generate lists on the fly with `[]`, you can generate mathematical sets on the fly with `{}`. This ensures uniqueness automatically.
```python
sentence = "functions,are,not,complicated"
words = sentence.split(',')

# Generates a set of words that have more than 2 unique vowels
unique_words = {word for word in words if len(set(word) & set("aeiouAEIOU")) > 2}
```

### Comprehension Logic: Mapping vs Filtering
The most common point of confusion in comprehensions is where to put the `if` statement. It entirely depends on whether you are **Filtering** (throwing items away) or **Mapping** (transforming items).

**1. Filtering (Trailing `if`)**
Use this when you want to completely skip/remove an item from the final list.
```python
# The 'if' goes at the VERY END. No 'else' is allowed.
palindromes = [w for w in words if w == w[::-1]]
```

**2. Mapping / Transforming (Leading `if/else`)**
Use this when you want to keep every single item, but conditionally change its value. Instead of copying a list and manually mutating it index-by-index, you map dynamically.
```python
# The 'if/else' goes at the VERY FRONT. An 'else' is STRICTLY REQUIRED.
# You can also chain them like an if-elif-else block!
results = ["Hot" if temp > 80 else "Cold" if temp < 50 else "Perfect" for temp in temps]

result = [item - 1 if item % 2 == 0 else item + 1 for item in items]
```

### Demystifying Nested List Comprehensions
Nested list comprehensions (like flattening a list of lists) feel backwards because the "kept item" is at the front. The trick is to **read the `for` loops from left to right**, exactly as they would be nested normally.

```python
# The Mental Translation:
# [ <what_to_keep> | <outer_loop> | <inner_loop> ]

lol = [[1, 2], [3, 4], [5, 6]]

# Normal loop:
# for inner_list in lol:
#     for item in inner_list:
#         result.append(item)

# Comprehension (Left-to-Right):
flat_list = [item for inner_list in lol for item in inner_list]
```
*(Note: If you don't need to manipulate the items and just want to flatten the list, `sum(lol, [])` is a highly readable alternative that uses the `+` operator to mathematically add the lists together!)*

### Generating 2D Matrices (Nested Comprehensions)
To safely generate an `n x m` grid in Python, you must use a nested comprehension `[[... for col] for row]`. 
*Warning: Never use `[[0]*m]*n` as it creates identical references to the same row in memory!*

```python
m = 3
# 1. Safe Initialization of an empty 3x3 grid
grid = [[0 for j in range(m)] for i in range(m)]

# 2. Advanced: Building an Identity Matrix using Mapping Logic
# Uses the exact same coordinates (i for row, j for col)
identity = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
```

### Generator Expressions and `next()`
If you write a comprehension using `()` instead of `[]` or `{}`, you are creating a **Generator Expression**, not a tuple! Generators are lazy iterables that evaluate one item at a time.

**1. Grabbing the FIRST match (Early Exit)**
If you only need to find a single item that matches a condition (like finding a specific node in a graph), wrap a generator expression in the built-in `next()` function. It evaluates until it finds the very first match, returns it, and instantly stops.
```python
# $O(1)$ early-exit instead of building a whole list!
first_even = next(x for x in numbers if x % 2 == 0)
```
*(Note: You can pass a default value `next(..., None)` so it doesn't throw a `StopIteration` error if no match is found).*

**2. "Tuple Comprehensions" (The Syntax Trap)**
Because `()` is reserved for Generators, there is no native tuple comprehension syntax! To generate a tuple, you must explicitly wrap a generator in the `tuple()` cast function.
```python
# ❌ Syntax Error: Python thinks you are passing two arguments to `tuple()`
# my_tuple = tuple(x, y for x, y in coordinates)

# ✅ Correct: You must yield a SINGLE item (a tuple wrapped in its own parentheses)
my_tuple = tuple((x, y) for x, y in coordinates)
```

---

## 6. Functions & OOP

### Functions & Arguments (`*args`)
Python functions are incredibly flexible.
```python
# 1. Default arguments
def greet(name="Guest"):
    print(f"Hello {name}")

# 2. Packing / Unpacking (*args)
# *args allows you to pass any number of positional arguments.
def mset(*args):
    # args is a tuple of all passed arguments
    print(args) 

mset("key1", "val1", "key2", "val2") # prints: ("key1", "val1", "key2", "val2")
```

### Object-Oriented Programming & Dunder Methods
Python OOP is fundamentally identical to Java, but with simpler syntax. 
- There is no `public/private` (we use a leading underscore `_` to signal "private by convention").
- `this` is called `self`, and you MUST pass it explicitly as the first argument to instance methods.

These are magic methods that let your objects behave like built-in Python types.
```python
class Database:
    def __init__(self):
        self.store = {"A": 1, "B": 2}
        
    def __len__(self):
        # Allows you to call `len(db)`!
        return len(self.store)
        
    def __str__(self):
        # Equivalent to Java's `toString()`
        return f"Database with {len(self)} items"

db = Database()
print(len(db)) # 2
print(db)      # "Database with 2 items"
```

---

## 7. Sorting (Advanced)

Sorting is a critical operation in many algorithms. Python's sort (`Timsort`) is **stable**.
```python
arr = [5, 2, 9, 1]

# 1. Ascending Sort
arr.sort()              # Mutates the list in-place (returns None)
new_arr = sorted(arr)   # Creates a BRAND NEW sorted list (arr remains unchanged)

# 2. Reverse (Descending) Sort
arr.sort(reverse=True)

# 3. Custom Sorting with Lambda (The `key` argument)
# Tell min/max/sorted exactly what to compare by returning a value from the lambda
students = [{"name": "Alice", "score": 90}, {"name": "Bob", "score": 95}]
top_student = max(students, key=lambda x: x["score"]) 

# Example: Sort strings by length, then alphabetically
words = ["banana", "apple", "kiwi", "pear"]
words.sort(key=lambda x: (len(x), x)) 
```

---

## 8. DSA Standard Library Highlights (NEW)

These built-in modules are indispensable for complex DSA problems:

* **`bisect`**: Python's binary search library.
  ```python
  import bisect
  bisect.bisect_left(arr, target) # Finds insertion point
  bisect.insort(arr, val)         # Inserts and maintains sorted order
  ```
* **`itertools`**: Combos, perms, and advanced iterators.
  ```python
  from itertools import permutations, accumulate, groupby
  
  perms = list(permutations([1, 2, 3]))
  
  # accumulate: Perfect for running totals (prefix sums) without a stateful for-loop
  running_totals = list(accumulate([1, 2, 3])) # [1, 3, 6]
  
  # groupby: The ultimate tool for finding "streaks" or grouping consecutive identical elements
  # Returns keys and iterator groups (must cast group to list to see contents)
  streaks = [list(g) for k, g in groupby([1, 1, 2, 1])] # [[1, 1], [2], [1]]
  ```
* **`math`**:
  ```python
  import math
  math.gcd(a, b)
  math.ceil(x)
  math.inf       # Same as float('inf')
  ```
* **`sys`**: Python's default recursion limit is 1000. For deep DFS, you **must** increase it!
  ```python
  import sys
  sys.setrecursionlimit(2500) 
  ```

---

## 9. Bitwise Operations

### Part A: The Fundamentals
You must understand what the operators do to binary strings.
*Let's assume A = 5 (0101 in binary) and B = 3 (0011 in binary).*

*   **AND (`&`):** Returns 1 if *both* bits are 1. (`5 & 3` = `1`)
*   **OR (`|`):** Returns 1 if *either* bit is 1. (`5 | 3` = `7`)
*   **XOR (`^`):** Returns 1 if bits are *different*. (`5 ^ 3` = `6`)
*   **NOT (`~`):** Flips all bits. `~5` = `-6`
*   **Left Shift (`<<`):** Shifts bits left (multiplies by 2). `5 << 1` = `10`
*   **Right Shift (`>>`):** Shifts bits right (floor division by 2). `5 >> 1` = `2`

### Part B: The 4 Essential Tricks
```python
# 1. The XOR Trick: A ^ A = 0
print(5 ^ 5)  # 0

# 2. Checking Even/Odd
n = 5
is_odd = (n & 1) == 1

# 3. Multiply / Divide by 2 instantly
val = 10 << 1 # 20

# 4. Clear the lowest set bit (Brian Kernighan’s algorithm)
n = 10 # 1010
n = n & (n - 1) # 1000 (8)
```

---

## 10. File Handling (The Pythonic Way)

Unlike Java's `BufferedReader`, Python uses `with open()` which automatically safely closes the file.

```python
with open('data.txt', 'r') as file:
    content = file.read()       

with open('output.txt', 'w') as file:
    file.write("Hello World!\n")
```
