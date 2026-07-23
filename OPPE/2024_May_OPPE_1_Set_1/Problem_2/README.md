# Problem 2

Given a list of strings, check if all strings follow the format where the same word is repeated exactly twice with a hyphen in-between them. The word repeated should not be empty.

### Examples
**Input:**
```
["fast-fast"]
```
**Output:**
```
True
```
**Explanation**
correct

**Input:**
```
["go-go"]
```
**Output:**
```
True
```
**Explanation**
correct

**Input:**
```
["yeah-yeah"]
```
**Output:**
```
True
```
**Explanation**
correct

**Input:**
```
["fast-slow"]
```
**Output:**
```
False
```
**Explanation**
incorrect (different words)

**Input:**
```
["fast-fast-fast"]
```
**Output:**
```
False
```
**Explanation**
incorrect (word repeated more than twice)

**Input:**
```
["fastfast"]
```
**Output:**
```
False
```
**Explanation**
incorrect (no hyphen)

**Input:**
```
["asfdadf"]
```
**Output:**
```
False
```
**Explanation**
incorrect (no hyphen, word not repeated)

**Input:**
```
["-"]
```
**Output:**
```
False
```
**Explanation**
incorrect (empty word)
