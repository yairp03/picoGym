# Obedient Cat

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 5

# Challenge

## Description

This file has a flag in plain sight (aka "in-the-clear"). [Download flag.](./flag)

## Source

[flag](./flag) (ASCII text)

# Solution

In this challenge, we're given a file named `flag`. We can use the [file](https://linux.die.net/man/1/file) command to determine the file type:

```bash
$ file flag
flag: ASCII text
```

The file is a text file, so we can open it in a text editor or print its contents to the terminal. Looking at the contents of the file, we can see that it contains the flag.

## Solution 1:

Open the `flag` file in a text editor.

## Solution 2:

Use the terminal [cat](https://linux.die.net/man/1/cat) command:

```bash
$ cat flag
picoCTF{s4n1ty_v3r1f13d_f28ac910}
```

**The Flag:** `picoCTF{s4n1ty_v3r1f13d_f28ac910}`
