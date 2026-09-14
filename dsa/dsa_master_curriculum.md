# DSA Mastery: The 15 Core Patterns & Tricks

Welcome to the unified Data Structures and Algorithms curriculum. This document acts as a **Cheatsheet for Specific Tricks and Patterns** to solve the LeetCode 150 problems in Python.

---

## 1. Arrays & Hashing Tricks

### The `ord()` Array Map Trick
When you need to count the frequency of lowercase English letters ('a' - 'z') without using a Hash Map, you can use an array of size 26.
*   `ord(char)` returns the integer ASCII value.
*   `ord(char) - ord('a')` maps 'a' to index 0, 'b' to 1, ..., 'z' to 25.
*   **Time Complexity:** $O(N)$

### Frequencies as Bucket Indices (Top K Problems)
When a problem asks for the "Most Frequent" or "Top K" elements, do not sort the Hash Map ($O(N \log N)$). Instead, use a modified **Bucket Sort**:
1.  Count frequencies with a Hash Map.
2.  Create an array of empty lists (buckets) of size `len(nums) + 1`.
3.  Let the **index** of the bucket represent the frequency.
4.  Iterate backwards through the buckets to gather the top elements in $O(N)$ time.

### `collections.defaultdict` vs `collections.Counter`
*   Use `defaultdict(list)` when you want to group items together (e.g., mapping a sorted string to a list of its anagrams). It avoids KeyError if the key doesn't exist yet.
*   Use `Counter(nums)` to instantly create a frequency map of an array in one line.

---

## 2. Two Pointers Tricks

### Squeezing from the Ends
For sorted arrays or palindromes, always initialize `L = 0` and `R = len(arr) - 1`. 
*   If the sum is too small, increment `L`.
*   If the sum is too big, decrement `R`.

---

## 3. Linked Lists Tricks

### The Dummy Node
Always initialize `dummy = ListNode(0, head)`. 
*   It eliminates edge cases when the head of the list might change or be deleted. 
*   Return `dummy.next` at the end.

### Fast and Slow Pointers (Floyd's Cycle Detection)
To find a cycle or the middle of a linked list:
```python
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

---

## 4. Trees Tricks

### DFS vs BFS
*   **DFS (Recursion):** Use when asked about depth, paths, or bottom-up aggregation.
*   **BFS (Queue):** Use `collections.deque`. Use when asked about levels (e.g., "Right side view", "Level order traversal").
