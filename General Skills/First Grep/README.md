# First Grep

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 100

# Challenge

## Description

Can you find the flag in [file](./file)? This would be really tedious to look through manually, something tells me there is a better way.

## Source

[file](./file) (ASCII text)

# Solution

Using `ls -l` command, we can see that the file is very large (14551 bytes):

```bash
$ ls -l file
-rw-r--r-- 1 yairp yairp 14551 Jan 19 15:57 file
```

Instead of looking through the file manually, we can use the `grep` command to search for the flag:

```bash
$ grep picoCTF file
picoCTF{grep_is_good_to_find_things_5af9d829}
```

**The Flag:** `picoCTF{grep_is_good_to_find_things_5af9d829}`
