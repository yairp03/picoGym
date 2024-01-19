# plumbing

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 200

# Challenge

## Description

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 4427`.

# Solution

Let's connect to the server:

```
$ nc jupiter.challenges.picoctf.org 4427
This is defintely not a flag
Not a flag either
...
I don't think this is a flag either
```

We get a lot of lines, and we can assume that one of them is the flag. We can use the `grep` command to search for the flag in the output:

```
$ nc jupiter.challenges.picoctf.org 4427 | grep picoCTF
picoCTF{digital_plumb3r_5ea1fbd7}
```

**The Flag:** `picoCTF{digital_plumb3r_5ea1fbd7}`
