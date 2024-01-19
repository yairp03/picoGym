# strings it

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 100

# Challenge

## Description

Can you find the flag in [file](./strings) without running it?

## Source

[strings](./strings) (ELF 64-bit)

# Solution

We got an ELF file. The title suggests that we should use the `strings` command to find the flag. The `strings` command prints all the printable strings in a file. Combining it with `grep` we can search for a specific string:

```bash
$ strings strings | grep picoCTF
picoCTF{5tRIng5_1T_7f766a23}
```

**The Flag:** `picoCTF{5tRIng5_1T_7f766a23}`
