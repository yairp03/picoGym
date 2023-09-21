# Lets Warm Up

**Author:** [yairp03](https://github.com/yaip03)  
**Category:** General Skills  
**Points:** 50

# Challenge

## Description

If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

# Solution

To answer this question, we can use python's builtin `chr` function, that converts a number to its ASCII character:

```python
> chr(0x70)
'p'
```

Wrapping the result in `picoCTF{}` gives us the flag.

**The Flag:** `picoCTF{p}`
