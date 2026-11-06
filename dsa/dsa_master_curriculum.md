# DSA Master Curriculum: Foundations, Complexities & The 14 Core Patterns

Welcome to the comprehensive Data Structures and Algorithms reference manual. This guide is built to serve two purposes:
1. Provide a rigorous, under-the-hood foundation of **Algorithmic Complexity & Python Runtime Internals** (essential for Senior, Lead, and Principal technical evaluations).
2. Detail the **14 Core Algorithmic Patterns** that power virtually all 150 LeetCode interview problems, complete with problem signals (triggers), canonical templates, and complexity proofs.

---

# PART I: Algorithmic Complexity & Python Internals

## 1. Asymptotic Notations: The Formal Definitions

| Notation | Meaning | Practical Interview Usage |
| :--- | :--- | :--- |
| **Big-O ($\mathcal{O}$)** | **Upper Bound:** $f(n) \le c \cdot g(n)$ for large $n$. | "Worst-case scenario" (the guaranteed ceiling). |
| **Big-Omega ($\Omega$)** | **Lower Bound:** $f(n) \ge c \cdot g(n)$ for large $n$. | "Best-case scenario" (the absolute minimum work required). |
| **Big-Theta ($\Theta$)** | **Tight Bound:** $c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n)$. | Precise behavior when best and worst cases match. |

> [!IMPORTANT]
> In interviews, when people say "Order of $N$", they almost always mean **Worst-Case Big-O**. Always clarify whether you are discussing average-case (e.g., QuickSort is $\mathcal{O}(N \log N)$ average, $\mathcal{O}(N^2)$ worst) or worst-case.

---

## 2. Complexity Classes & The "Input Size Rule of Thumb"

An interviewer often won't tell you the required time complexity, but the **constraints** in the problem statement give it away immediately:

| Constraint Size ($N$) | Maximum Allowed Complexity | Typical Algorithmic Paradigm |
| :--- | :--- | :--- |
| $N \le 10 - 12$ | $\mathcal{O}(N!)$ or $\mathcal{O}(N^2 \cdot 2^N)$ | Permutations, Traveling Salesperson, Brute Backtracking |
| $N \le 20 - 25$ | $\mathcal{O}(2^N)$ | Subsets, Combinations, Bitmask Dynamic Programming |
| $N \le 100 - 500$ | $\mathcal{O}(N^3)$ | Floyd-Warshall (All-Pairs Shortest Path), 3D DP |
| $N \le 2,000 - 5,000$ | $\mathcal{O}(N^2)$ | Nested loops, 2D DP, Insertion/Bubble Sort, All Pairs |
| $N \le 10^5 - 2 \cdot 10^5$ | $\mathcal{O}(N \log N)$ or $\mathcal{O}(N)$ | Sorting, Heaps, Divide & Conquer, Two Pointers, Sliding Window, Monotonic Stack |
| $N \le 10^7 - 10^8$ | $\mathcal{O}(N)$ | Single pass, Hash Table, Bit manipulation |
| $N \ge 10^9$ | $\mathcal{O}(\log N)$ or $\mathcal{O}(1)$ | Binary Search, Math, Euclidean GCD, Matrix Exponentiation |

*Rule of thumb:* Modern interview environments and online judges execute roughly **$10^7$ to $10^8$ operations per second**. If your algorithm exceeds $10^8$ operations for the max constraint, expect a Time Limit Exceeded (TLE).

---

## 3. Space Complexity & Memory Mechanics

Space complexity measures **Auxiliary Memory**—extra memory allocated by your algorithm relative to input size:
1. **Auxiliary Data Structures:** Hash maps, sets, queues, arrays ($\mathcal{O}(N)$).
2. **The Call Stack (Recursion):** Every recursive function call places a stack frame in memory.
   * A balanced binary tree recursion of depth $\log N$ takes $\mathcal{O}(\log N)$ stack space.
   * A degenerate tree (skewed linked-list style) takes $\mathcal{O}(N)$ stack space.
   * **Common pitfall:** An algorithm with zero auxiliary lists still consumes $\mathcal{O}(N)$ space if its recursion depth is $N$!
3. **In-Place Modification ($\mathcal{O}(1)$ Auxiliary Space):** Mutating the input array or pointer links directly without allocating secondary arrays.

---

## 4. Amortized Analysis: Why `list.append()` is $\mathcal{O}(1)$

An operation has **Amortized $\mathcal{O}(1)$** time if an occasional expensive operation is paid for by many cheap ones.
* **Python's Dynamic Array Resizing:**
  * When you initialize `arr = []`, Python allocates a small fixed block of memory.
  * When full, `arr.append(x)` allocates a new contiguous buffer roughly **$1.125 \times$ to $1.25 \times$** larger (geometric growth) and copies all elements over ($\mathcal{O}(N)$ work).
  * Because this copying happens exponentially less frequently as $N$ grows, the average cost across $N$ appends is $\mathcal{O}(1)$.
* **Lead/Principal Discussion Point:** In latency-critical systems (e.g., high-frequency trading or real-time event streaming), amortized $\mathcal{O}(1)$ is a liability because resizing causes **p99 latency spikes**. Fixed-size pre-allocated buffers (or circular ring buffers) are used to eliminate these spikes.

---

## 5. Python Runtime Gotchas & Performance Anti-Patterns

| Anti-Pattern (Slow) | Fast Idiom | Why It Matters Under the Hood |
| :--- | :--- | :--- |
| `queue.pop(0)` ($\mathcal{O}(N)$) | `from collections import deque`<br>`queue.popleft()` ($\mathcal{O}(1)$) | Python lists are contiguous arrays; `pop(0)` shifts every subsequent element left by 1. `deque` is a doubly-linked block list. |
| `sub = arr[i:j]` ($\mathcal{O}(K)$) | Use index pointers (`left`, `right`) | Slicing creates a **shallow copy** of the slice ($K = j - i$ items). Doing `arr[1:]` in a recursive loop creates an accidental $\mathcal{O}(N^2)$ algorithm! |
| String concatenation in loop:<br>`s += char` ($\mathcal{O}(N^2)$) | `chars.append(char)`<br>`''.join(chars)` ($\mathcal{O}(N)$) | Python strings are **immutable**. `s += char` reallocates a brand-new string and copies all previous characters each time. |
| Lookup in list:<br>`if x in my_list:` ($\mathcal{O}(N)$) | `if x in my_set:` ($\mathcal{O}(1)$ avg) | Lists require linear scanning. Sets use open-address hash tables with near-constant lookup. |
| `sorted(arr)` | `arr.sort()` | `sorted()` creates a brand-new list ($\mathcal{O}(N)$ space). `arr.sort()` sorts in-place using **Timsort** ($\mathcal{O}(N \log N)$ worst, $\mathcal{O}(N)$ best for nearly-sorted). |

---

# PART II: The 14 Core Algorithmic Patterns

---

## 1. Arrays & Hashing (Prefix Sums, Complements, Bucket Sort)

### Mental Model & Intuition
Trade space for time. By remembering what we have already seen via a Hash Set or Hash Map, we can eliminate nested searching loops.
* **Complement Lookup:** Instead of searching for $Y$ such that $X + Y = \text{target}$, look up $\text{target} - X$ in $\mathcal{O}(1)$ time.
* **Prefix Sums:** Precompute running sums `prefix[i] = prefix[i-1] + nums[i]`. The sum of any subarray `nums[i...j]` is simply `prefix[j] - prefix[i-1]`, calculated in $\mathcal{O}(1)$ time.

### Triggers & Problem Signals
* "Find two numbers that add up to $K$" (Unsorted array $\rightarrow$ Hash Map; Sorted array $\rightarrow$ Two Pointers).
* "Subarray sum equals $K$ with negative numbers included" $\rightarrow$ Prefix Sums + Hash Map.
* "Find top $K$ frequent elements in $\mathcal{O}(N)$ time" $\rightarrow$ Bucket Sort (frequencies as indices).
* "Check for duplicates or anagrams" $\rightarrow$ Hash Map or frequency array.

### Specific Arrays & Hashing Tricks

#### 1. The `ord()` Array Map Trick
When you need to count the frequency of lowercase English letters ('a' - 'z') without using a Hash Map, you can use an array of size 26:
* `ord(char)` returns the integer ASCII value.
* `ord(char) - ord('a')` maps 'a' to index 0, 'b' to 1, ..., 'z' to 25.
* **Time Complexity:** $\mathcal{O}(N)$, **Space Complexity:** $\mathcal{O}(1)$ (fixed 26-element array).

#### 2. Frequencies as Bucket Indices (Top K Problems)
When a problem asks for the "Most Frequent" or "Top K" elements, do not sort the Hash Map ($\mathcal{O}(N \log N)$). Instead, use a modified **Bucket Sort**:
1. Count frequencies with a Hash Map.
2. Create an array of empty lists (buckets) of size `len(nums) + 1`.
3. Let the **index** of the bucket represent the frequency.
4. Iterate backwards through the buckets to gather the top elements in $\mathcal{O}(N)$ time.

#### 3. `collections.defaultdict` vs `collections.Counter`
* Use `defaultdict(list)` when you want to group items together (e.g., mapping a sorted string to a list of its anagrams). It avoids KeyError if the key doesn't exist yet.
* Use `Counter(nums)` to instantly create a frequency map of an array in one line.

### Canonical Python Template (Prefix Sum with Hash Map)
```python
def subarray_sum_k(nums: list[int], k: int) -> int:
    prefix_count = {0: 1}  # Base case: a prefix sum of 0 has occurred once
    current_sum = 0
    count = 0
    for x in nums:
        current_sum += x
        # If (current_sum - k) was seen before, a valid subarray ends here
        if current_sum - k in prefix_count:
            count += prefix_count[current_sum - k]
        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
    return count
```
* **Time Complexity:** $\mathcal{O}(N)$ — single pass with $\mathcal{O}(1)$ dictionary operations.
* **Space Complexity:** $\mathcal{O}(N)$ — to store up to $N$ distinct prefix sums.

---

## 2. Two Pointers (Squeeze from Ends & Partitioning)

### Mental Model & Intuition
Use monotonic properties (sorted order or symmetry) to eliminate search space without checking every combination.
* **Opposite Direction:** Start at index `0` and `N-1`. Move pointers toward each other based on comparison.
* **Same Direction (Slow/Fast):** Slow pointer tracks write-position (e.g., removing duplicates in-place), fast pointer scans ahead.

### Triggers & Problem Signals
* "Array is sorted, find a pair/triplet" (e.g., Two Sum II, 3Sum).
* "Palindrome verification or reversal".
* "Container with Most Water / Trapping Rain Water".
* "Modify array in-place with $\mathcal{O}(1)$ space" (e.g., Move Zeroes, Remove Duplicates).

### Canonical Python Template (Opposite Direction Squeeze)
```python
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1   # Need a larger sum
        else:
            right -= 1  # Need a smaller sum
    return []
```
* **Time Complexity:** $\mathcal{O}(N)$ — each iteration moves at least one pointer inward; total steps $\le N$.
* **Space Complexity:** $\mathcal{O}(1)$ — constant extra variables.

---

## 3. Sliding Window (Fixed vs. Dynamic Invariant)

### Mental Model & Intuition
Instead of recalculating overlapping subsegment metrics from scratch ($\mathcal{O}(N \cdot K)$), maintain a continuous window $[L, R]$. When $R$ moves right, absorb the incoming element. When the window becomes invalid, advance $L$ to restore the invariant.

### Triggers & Problem Signals
* "Contiguous subarray / substring" satisfying a condition (max/min sum, at most $K$ distinct elements, longest substring without repeating characters).
* **Crucial Rule:** All elements must generally be **non-negative** if tracking sums, because non-negativity guarantees that advancing $R$ monotonically increases the sum and advancing $L$ monotonically decreases it.

### Canonical Python Template (Dynamic Invariant Window)
```python
def length_of_longest_substring(s: str) -> int:
    char_map = {}  # char -> last seen index
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1  # Jump left pointer past previous occurrence
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```
* **Time Complexity:** $\mathcal{O}(N)$ — both $L$ and $R$ traverse the string at most once.
* **Space Complexity:** $\mathcal{O}(\min(N, \Sigma))$ — where $\Sigma$ is the alphabet size (e.g., 26 or 128).

---

## 4. Stack & Monotonic Stack

### Mental Model & Intuition
* **Standard Stack (LIFO):** Ideal for parsing nested structures, matching brackets, or undo operations.
* **Monotonic Stack:** Maintains elements in strictly increasing or decreasing order. Whenever a new incoming element violates the monotonic order, elements are popped. The popped element's "next greater" or "previous smaller" element is precisely the incoming element!

### Triggers & Problem Signals
* "Valid parentheses / balanced expression parsing".
* "Find the Next Greater Element / Previous Smaller Element" (e.g., Daily Temperatures).
* "Largest Rectangle in Histogram / Online Stock Span".

### Canonical Python Template (Monotonic Decreasing Stack)
```python
def daily_temperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    result = [0] * n
    stack = []  # Stores indices: temperatures[i] will be strictly decreasing
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)
    return result
```
* **Time Complexity:** $\mathcal{O}(N)$ — each index is pushed onto the stack exactly once and popped at most once.
* **Space Complexity:** $\mathcal{O}(N)$ — worst-case stack holds all elements if strictly decreasing.

---

## 5. Binary Search (Value Search & Binary Search on Answer)

### Mental Model & Intuition
Repeatedly halve a monotonic search space.
* **Classic Search:** Locating an element in a sorted list.
* **Binary Search on the Answer Space:** When asked to find the minimum/maximum feasible value $X$ (e.g., "minimum capacity to ship packages within $D$ days"), and you can write a monotonic verification function `can_ship(capacity) -> bool`, binary search on the possible capacities from $1$ to $\sum \text{weights}$!

### Triggers & Problem Signals
* "Array is sorted or rotated sorted" with requirement of $\mathcal{O}(\log N)$ time.
* "Find the minimum of maximums / maximum of minimums" (e.g., Koko Eating Bananas, Split Array Largest Sum).

### Canonical Python Template (Standard Upper/Lower Bound Safe Template)
```python
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Prevents integer overflow in languages like C++/Java
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
* **Time Complexity:** $\mathcal{O}(\log N)$ — search space is divided by 2 at each step.
* **Space Complexity:** $\mathcal{O}(1)$ — constant variables.

---

## 6. Linked Lists (Dummy Head, Pointer Reversal, Fast/Slow)

### Mental Model & Intuition
Linked lists are dynamic collections linked by pointers.
* **Dummy Head:** `dummy = ListNode(0, head)`. Eliminates edge cases where the head itself needs to be removed, replaced, or merged.
* **In-Place Reversal:** Maintain `prev`, `curr`, `next_node` pointers.
* **Fast and Slow Pointers (Floyd's Cycle Finding):** Fast moves 2 steps, Slow moves 1 step. If they meet, there is a cycle. If `fast` hits `None`, there is no cycle.
```python
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # Cycle detected
return False
```

### Triggers & Problem Signals
* "Reverse a linked list (or sublist from $M$ to $N$)".
* "Detect a cycle or find the cycle entrance node".
* "Find the middle of a linked list in a single pass".
* "Merge $K$ sorted lists or reorder list".

### Canonical Python Template (In-Place Reversal)
```python
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```
* **Time Complexity:** $\mathcal{O}(N)$ — single traversal.
* **Space Complexity:** $\mathcal{O}(1)$ — in-place pointer rewriting.

---

## 7. Trees & Binary Search Trees (DFS, BFS, BST Invariants)

### Mental Model & Intuition
* **DFS vs BFS:**
  * **DFS (Recursion):** Use when asked about depth, paths, subtree validation, or bottom-up aggregation.
  * **BFS (Queue):** Use `collections.deque`. Use when asked about levels (e.g., "Right side view", "Level order traversal", "Minimum depth to leaf").
* **Binary Search Tree (BST) Property:** `left.val < root.val < right.val`. In-order traversal visits nodes in strictly sorted ascending order!

### Triggers & Problem Signals
* "Level order traversal / zigzag view" $\rightarrow$ BFS with `collections.deque`.
* "Validate BST" $\rightarrow$ In-order traversal or recursive range $[low, high]$.
* "Lowest Common Ancestor" $\rightarrow$ Post-order DFS.
* "Diameter / Max Path Sum" $\rightarrow$ Post-order DFS returning height, updating global max.

### Canonical Python Template (BFS Level Order Traversal)
```python
from collections import deque

def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level_nodes)
    return result
```
* **Time Complexity:** $\mathcal{O}(N)$ — visits each node exactly once.
* **Space Complexity:** $\mathcal{O}(W)$ where $W$ is the maximum width of the tree (up to $N/2$ for full binary tree $\rightarrow \mathcal{O}(N)$).

---

## 8. Heap / Priority Queue (Top-K & Streaming)

### Mental Model & Intuition
A complete binary tree maintained in an array where the root is always the minimum (min-heap) or maximum (max-heap).
* **Heapify:** Building a heap from an unsorted array takes $\mathcal{O}(N)$ time (sifting down), NOT $\mathcal{O}(N \log N)$!
* **Maintaining Top $K$ Elements:** Use a **Min-Heap of fixed size $K$**. Push incoming items; if size exceeds $K$, pop the minimum. At the end, the root is the $K$-th largest element!

### Triggers & Problem Signals
* "Find the $K$-th largest / smallest element in an array or data stream".
* "Merge $K$ sorted lists".
* "Find median from data stream" $\rightarrow$ Two heaps (Max-heap for lower half, Min-heap for upper half).

### Canonical Python Template (K-th Largest using Min-Heap)
```python
import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    min_heap = []
    for x in nums:
        heapq.heappush(min_heap, x)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
```
* **Time Complexity:** $\mathcal{O}(N \log K)$ — pushing/popping into a heap of size $K$ costs $\mathcal{O}(\log K)$.
* **Space Complexity:** $\mathcal{O}(K)$ — heap size never exceeds $K + 1$.

---

## 9. Backtracking (Combinatorial State Exploration)

### Mental Model & Intuition
Brute-force depth-first exploration with **pruning**. Build a candidate solution incrementally; as soon as a candidate cannot lead to a valid full solution, discard it ("backtrack") by undoing the last choice.

### Universal Template Structure
```python
def backtrack(candidate, state):
    if is_solution(candidate):
        output(candidate)
        return
    for choice in valid_choices(state):
        make_choice(choice)       # 1. Choose
        backtrack(candidate, state) # 2. Explore
        undo_choice(choice)       # 3. Unchoose / Backtrack
```

### Triggers & Problem Signals
* "Generate all permutations / combinations / subsets".
* "N-Queens, Sudoku Solver, Word Search on Grid".
* Constraints are small ($N \le 12 - 20$).

### Canonical Python Template (Subsets)
```python
def subsets(nums: list[int]) -> list[list[int]]:
    result = []
    path = []
    def dfs(start_idx: int):
        result.append(list(path))  # Snapshot current subset
        for i in range(start_idx, len(nums)):
            path.append(nums[i])   # Choose
            dfs(i + 1)             # Explore
            path.pop()             # Backtrack
    dfs(0)
    return result
```
* **Time Complexity:** $\mathcal{O}(N \cdot 2^N)$ — $2^N$ total subsets, each taking up to $\mathcal{O}(N)$ to copy.
* **Space Complexity:** $\mathcal{O}(N)$ — recursion depth and `path` array.

---

## 10. Graphs: Traversals & Topological Sort

### Mental Model & Intuition
A collection of vertices ($V$) connected by edges ($E$).
* **Matrix as Graph:** Grid problems (e.g., Number of Islands) are graphs where every cell $(r, c)$ has up to 4 neighbors.
* **Topological Sort (Kahn's Algorithm):** Direct Acyclic Graph (DAG) task scheduling. Count in-degrees (incoming prerequisites). Place nodes with 0 in-degrees into a queue. As nodes are processed, decrement neighbor in-degrees. If processed nodes $< |V|$, a cycle exists!

### Triggers & Problem Signals
* "Connected components, island counts, flood fill" $\rightarrow$ DFS or BFS.
* "Shortest path in unweighted graph" $\rightarrow$ BFS.
* "Course Schedule / Build Dependency Order" $\rightarrow$ Topological Sort.
* "Shortest path in weighted graph with non-negative weights" $\rightarrow$ Dijkstra ($\mathcal{O}((V + E) \log V)$).

### Canonical Python Template (Kahn's Topological Sort)
```python
from collections import deque, defaultdict

def course_schedule(num_courses: int, prerequisites: list[list[int]]) -> bool:
    adj = defaultdict(list)
    in_degree = [0] * num_courses
    for course, prereq in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1
        
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    completed = 0
    while queue:
        curr = queue.popleft()
        completed += 1
        for neighbor in adj[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return completed == num_courses
```
* **Time Complexity:** $\mathcal{O}(V + E)$ — each vertex and edge visited once.
* **Space Complexity:** $\mathcal{O}(V + E)$ — adjacency list and in-degree array.

---

## 11. Disjoint Set Union (DSU / Union-Find)

### Mental Model & Intuition
Tracks a set of elements partitioned into non-overlapping subsets.
* **Find with Path Compression:** Flattens the tree so every node points directly to the set representative.
* **Union by Rank:** Always attaches the shorter tree under the taller tree, keeping trees flat.
* **Combined Complexity:** Operations run in near-constant time: $\mathcal{O}(\alpha(N))$, where $\alpha$ is the Inverse Ackermann function (for all practical purposes, $\alpha(N) \le 4$).

### Triggers & Problem Signals
* "Dynamic connectivity / incremental edge additions".
* "Find cycle in undirected graph".
* "Redundant Connection, Kruskal's Minimum Spanning Tree, Number of Connected Components".

### Canonical Python Template
```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False  # Already connected: cycle detected!
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.rank[root_x] += self.rank[root_y]
        return True
```
* **Time Complexity:** $\mathcal{O}(\alpha(N)) \approx \mathcal{O}(1)$ per operation.
* **Space Complexity:** $\mathcal{O}(N)$ — parent and rank arrays.

---

## 12. Dynamic Programming (1D & 2D)

### Mental Model & Intuition
Break a problem down into overlapping subproblems with optimal substructure.
* **Top-Down (Memoization):** Recursive DFS + caching results in a hash table or array.
* **Bottom-Up (Tabulation):** Iterative array filling from base cases up to target.
* **Space Optimization:** If `dp[i]` only depends on `dp[i-1]` and `dp[i-2]`, eliminate the array and keep only two variables ($\mathcal{O}(1)$ space!).

### Triggers & Problem Signals
* "Count the number of ways to reach...", "Find minimum cost / maximum profit".
* "Choice at each step affects future choices (cannot be solved with Greedy)".
* Common categories:
  - 1D: Climbing stairs, House Robber, Coin Change.
  - 2D Strings: Longest Common Subsequence, Edit Distance.
  - 2D Grids: Unique Paths, Minimum Path Sum.
  - Knapsack: 0/1 Knapsack (items used once), Unbounded Knapsack (items reused).

### Canonical Python Template (1D Coin Change - Minimum Coins)
```python
def coin_change(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```
* **Time Complexity:** $\mathcal{O}(\text{amount} \times \text{len(coins)})$.
* **Space Complexity:** $\mathcal{O}(\text{amount})$ — 1D DP table.

---

## 13. Greedy & Intervals

### Mental Model & Intuition
* **Greedy:** Make the locally optimal choice at every step without backtracking. Works ONLY when local optimality guarantees global optimality (e.g., Jump Game, Gas Station).
* **Intervals:** Always sort intervals by their start time (`intervals.sort(key=lambda x: x[0])`). Check if current interval overlaps with previous interval (`curr[0] <= prev[1]`).

### Triggers & Problem Signals
* "Merge intervals, insert interval, non-overlapping intervals, meeting rooms".
* "Task Scheduler / Gas Station".

### Canonical Python Template (Merge Intervals)
```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
```
* **Time Complexity:** $\mathcal{O}(N \log N)$ — due to sorting.
* **Space Complexity:** $\mathcal{O}(N)$ — output list (or $\mathcal{O}(\log N)$ auxiliary for sorting).

---

## 14. Bit Manipulation

### Mental Model & Intuition
Bit manipulation operates directly on binary representation at hardware register speeds ($\mathcal{O}(1)$).
* **XOR ($\oplus$):**
  - $x \oplus 0 = x$
  - $x \oplus x = 0$
  - Commutative & associative. XORing all numbers in a list cancels out every duplicate that appears an even number of times, leaving only the unique element!
* **Brian Kernighan's Trick (`n & (n - 1)`):** Clears the lowest set bit. Repeat until $n = 0$ to count set bits in time proportional to the number of 1s!
* **Bit Shifts:** `1 << k` sets the $k$-th bit. `(n >> k) & 1` checks if the $k$-th bit is set.

### Triggers & Problem Signals
* "Find the single number when all others appear twice" $\rightarrow$ XOR.
* "Count number of 1 bits (Hamming Weight)" $\rightarrow$ `n & (n - 1)`.
* "Bitwise AND of numbers range" or "Missing number in range $0...N$".

### Canonical Python Template (Counting Set Bits)
```python
def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)  # Clears the lowest set bit
        count += 1
    return count
```
* **Time Complexity:** $\mathcal{O}(B)$ where $B$ is the number of set bits (at most 32 or 64 iterations, i.e., $\mathcal{O}(1)$).
* **Space Complexity:** $\mathcal{O}(1)$.
