# DSA Mastery: The 15 Core Patterns

Welcome to your unified Data Structures and Algorithms curriculum. This document provides the exact mental models you need to solve the NeetCode 150 problems in Python.

---

## 0. Zero to Hero: Fundamentals

### Big-O Notation (Time & Space Complexity)
Before you write any code, you need to know how to talk about its efficiency. Big-O ignores hardware speed and focuses purely on **how the algorithm scales** as the input size ($N$) grows.

*   **$O(1)$ - Constant Time:** The holy grail. The operation takes the exact same amount of time regardless of how big the input is.
    *   *Example:* Looking up a value in a Hash Map by its key, or getting the first item of an array `arr[0]`.
*   **$O(N)$ - Linear Time:** The time scales directly with the input. If the array is 10x bigger, it takes 10x longer.
    *   *Example:* A standard `for` loop iterating through an array.
*   **$O(N^2)$ - Quadratic Time:** The danger zone. If the array is 10x bigger, it takes 100x longer. You will almost always fail an interview if you submit an $O(N^2)$ solution when an $O(N)$ exists.
    *   *Example:* Nested `for` loops (checking every element against every other element).
*   **$O(\\log N)$ - Logarithmic Time:** Extremely fast for large datasets. The algorithm halves the search space at every step.
    *   *Example:* Binary Search. Searching 1,000,000 sorted items takes at most 20 steps!

### Hashing 101: How Hash Maps Work
A Hash Map (Python `dict`) allows you to store and retrieve data in **$O(1)$ Constant Time**. How is that possible without scanning the entire memory?
1.  **The Array:** Under the hood, a Hash Map is literally just an array of a fixed size (e.g., size 10).
2.  **The Hash Function:** When you save `map["Alice"] = 25`, the string `"Alice"` is passed through a mathematical **Hash Function** which spits out a pseudo-random integer, say `8`.
3.  **The Storage:** The map instantly goes to index `8` of its internal array and drops the value `25` there.
4.  **The Retrieval:** When you ask for `map["Alice"]`, it hashes `"Alice"` again, gets `8`, goes straight to index `8`, and grabs the data instantly. No looping required!

---

## 0. Zero to Hero: Fundamentals

### Big-O Notation (Time & Space Complexity)
Before you write any code, you need to know how to talk about its efficiency. Big-O ignores hardware speed and focuses purely on **how the algorithm scales** as the input size ($N$) grows.

*   **$O(1)$ - Constant Time:** The holy grail. The operation takes the exact same amount of time regardless of how big the input is.
    *   *Example:* Looking up a value in a Hash Map by its key, or getting the first item of an array `arr[0]`.
*   **$O(N)$ - Linear Time:** The time scales directly with the input. If the array is 10x bigger, it takes 10x longer.
    *   *Example:* A standard `for` loop iterating through an array.
*   **$O(N^2)$ - Quadratic Time:** The danger zone. If the array is 10x bigger, it takes 100x longer. You will almost always fail an interview if you submit an $O(N^2)$ solution when an $O(N)$ exists.
    *   *Example:* Nested `for` loops (checking every element against every other element).
*   **$O(\\log N)$ - Logarithmic Time:** Extremely fast for large datasets. The algorithm halves the search space at every step.
    *   *Example:* Binary Search. Searching 1,000,000 sorted items takes at most 20 steps!

### Hashing 101: How Hash Maps Work
A Hash Map (Python `dict`) allows you to store and retrieve data in **$O(1)$ Constant Time**. How is that possible without scanning the entire memory?
1.  **The Array:** Under the hood, a Hash Map is literally just an array of a fixed size (e.g., size 10).
2.  **The Hash Function:** When you save `map["Alice"] = 25`, the string `"Alice"` is passed through a mathematical **Hash Function** which spits out a pseudo-random integer, say `8`.
3.  **The Storage:** The map instantly goes to index `8` of its internal array and drops the value `25` there.
4.  **The Retrieval:** When you ask for `map["Alice"]`, it hashes `"Alice"` again, gets `8`, goes straight to index `8`, and grabs the data instantly. No looping required!

---

## 1. Arrays & Hashing

**The Core Concept:**
Arrays are contiguous blocks of memory. Hash Maps (Dictionaries) allow O(1) lookups by hashing a key to an index.

**When to use a Hash Map/Set:**
*   You need to check if you have seen an element before in O(1) time.
*   You need to count frequencies of elements.

**The Golden Rule:** If a brute force solution requires `O(N^2)` time because you have to loop through the array to find a pair, you can almost always reduce it to `O(N)` time and `O(N)` space by using a Hash Map to store elements you've already seen.

**NeetCode 150 Focus Problems:**
*   *Contains Duplicate* (Use a HashSet)
*   *Valid Anagram* (Use a HashMap frequency counter, or `collections.Counter`)
*   *Two Sum* (Store `target - num` in a HashMap as you iterate)

---

## 2. Two Pointers

**The Core Concept:**
Use two variables (pointers) to traverse an array or string from different ends or at different speeds.

**When to use Two Pointers:**
*   The array is **sorted** and you need to find a pair that meets a condition.
*   You need to reverse a string or array in-place.
*   You are dealing with Palindromes.

**The Golden Rule:** A sorted array is the biggest hint for a Two Pointer approach. Start one pointer at `L = 0` and the other at `R = len(arr) - 1`. If the sum is too small, `L += 1`. If the sum is too big, `R -= 1`.

**NeetCode 150 Focus Problems:**
*   *Valid Palindrome* (L at start, R at end, squeeze inward)
*   *Two Sum II* (Sorted input -> L and R pointers)

---

## 3. Linked Lists

**The Core Concept:**
Nodes connected by pointers. Unlike arrays, they are not contiguous in memory, so you cannot access `node[3]` in O(1) time.

**The Golden Rule:** Always use a `dummy` node pointing to the head when you might need to modify the head of the list. It eliminates edge cases. For cycle detection, always use a slow pointer (`slow = slow.next`) and a fast pointer (`fast = fast.next.next`).

**NeetCode 150 Focus Problems:**
*   *Reverse Linked List* (Keep track of `prev`, `curr`, and `nxt`)
*   *Merge Two Sorted Lists* (Use a `dummy` node)
*   *Linked List Cycle* (Fast and Slow pointers)

---

## 4. Trees

**The Core Concept:**
Non-linear data structures. Almost every Tree problem is solved using Recursion (DFS) or a Queue (BFS).

**The Golden Rule:**
If the problem asks about depth, paths, or bottom-up aggregation, use **DFS (Recursion)**.
If the problem asks about levels (e.g., "Right side view", "Level order traversal"), use **BFS (Queue with `collections.deque`)**.

**NeetCode 150 Focus Problems:**
*   *Invert Binary Tree* (Swap left and right, recurse)
*   *Maximum Depth of Binary Tree* (`1 + max(dfs(left), dfs(right))`)
*   *Same Tree* (Check if current nodes match, then recurse left and right)
