# Static ain't always noise

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 20

# Challenge

## Description

Can you look at the data in this binary: [static](./static)? This [BASH script](./ltdis.sh) might help!

## Source

[static](./static) (ELF 64-bit)  
[ltdis.sh](./ltdis.sh) (Bash script)

# Solution

We got a `ELF` file, but running it doesn't give us anything useful:

```bash
$ ./static
Oh hai! Wait what? A flag? Yes, it's around here somewhere!
```

The flag should be somewhere in the file, but it's not printed. Let's find it.

## Solution 1:

We can disassemble it using [ltdis.sh](./ltdis.sh):

```bash
$ ./ltdis.sh static
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
```

The script created a file called `static.ltdis.strings.txt` which contains all the strings in the binary, and if we look at it, we can see the flag:

```bash
$ cat static.ltdis.strings.txt | grep pico
picoCTF{d15a5m_t34s3r_98d35619}
```

## Solution 2:

The bash scripts actually runs the [strings](https://linux.die.net/man/1/strings) command on the binary, so we can just run it ourselves:

```bash
$ strings static | grep pico
picoCTF{d15a5m_t34s3r_98d35619}
```

**The Flag:** `picoCTF{d15a5m_t34s3r_98d35619}`
