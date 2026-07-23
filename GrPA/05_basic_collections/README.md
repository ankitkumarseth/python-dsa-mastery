# GrPA Basic Collections

## A Bit of Wisdom

* **Iterable** – Something that can be used in a `for` loop.
* **Collection** – Datatypes that hold many values like `list`, `set`, `tuple`, and `dict`.
  * *All iterables are not collections.* For example, `str` and `range` are iterables but not collections.
  * *All collections are iterables.*
* Only ordered collections are indexable and slicable.
* Only mutable collections can be modified.
* Hashing is a method used in collections like `set` to check whether an element is present quickly, and in `dict` to retrieve the value for a given key efficiently. Only certain data types can be hashed.

| Data Type | Iterable | Collection | Indexable / Slicable | Ordered | Mutable | Uses Hashing |
|-----------|----------|------------|----------------------|---------|---------|--------------|
| `str`     | ✅        | ❌          | ✅                    | ✅       | ❌       | ❌            |
| `range`   | ✅        | ❌          | ❌                    | ✅       | ❌       | ❌            |
| `list`    | ✅        | ✅          | ✅                    | ✅       | ✅       | ❌            |
| `tuple`   | ✅        | ✅          | ✅                    | ✅       | ❌       | ❌            |
| `set`     | ✅        | ✅          | ❌                    | ❌       | ✅       | ✅            |
| `dict`    | ✅        | ✅          | ❌                    | ❌       | ✅       | ✅ (on keys)  |

* **Built-in functions** – Functions like `sum()`, `min()`, `max()`, `sorted()`, and `reversed()` help perform common operations on collections.
* Any iterable can be converted into a `list` or a `tuple`.
* Any iterable containing hashable data types can be converted into a `set`.

## Learning Objectives
*(Note: In this exercise, we will not be using `dict`, as it will be introduced in the next week.)*

* Empty collections
* Singleton collections
* Truthiness and falsiness of collections
* Built-in functions for collections
* Indexing and slicing
* Membership checks
* Concatenation

## Example Test Cases
When the evaluator runs your script, they will inject global variables. Here are some examples of what values they expect your populated variables to hold based on the injected variables:

### Examples
**Input:**
```python
int_iterable = [4, 2, 4, 6, 7, 3, -2, 3]
# Your variables should evaluate to:
int_iterable_min == -2
int_iterable_reversed == [3, -2, 3, 7, 6, 4, 2, 4]
```
**Output:**
```text

```
> 
### Examples
**Input:**
```python
some_collection = tuple(range(10))
# Your variables should evaluate to:
third_last_element == 7
odd_index_elements == (1, 3, 5, 7, 9)
```
**Output:**
```text

```
>
### Examples
**Input:**
```python
string_iterable = {"Banana", "Mango", "Cherry", "Apple"}
# Your variables should evaluate to:
all_concat == 'Apple-Banana-Cherry-Mango'
```
**Output:**
```text

```

> [!WARNING]
> **NOTE:** You should not use `for` loops or the word `for` anywhere in this exercise!
