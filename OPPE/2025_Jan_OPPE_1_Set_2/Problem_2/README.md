# Check String Rotation

Write a function that checks if one string is a rotation of another.

*Hint: all the rotations of a particular string will be present in the string formed by concatenating it with itself.*

For example the rotations of the word `apple` can be formed by:
- `a[pplea]pple` - `pplea`
- `ap[pleap]ple` - `pleap`
- `app[leapp]le` - `leapp`
- `appl[eappl]e` - `eappl`
- `apple[apple]` - `apple`

**NOTE:** This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

### Example

```python
>>>is_rotation('abcde','cdeab')
True
>>>is_rotation('hello','ehllo')
False
>>>is_rotation('hello','helol')
False
```
**Explanation:**
Since `cdeab` is a rotation of `abcde`,
So, `is_rotation('abcde','cdeab')` should return `True`
