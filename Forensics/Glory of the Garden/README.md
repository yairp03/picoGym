# Glory of the Garden

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Forensics  
**Points:** 50

# Challenge

## Description

This [garden](./garden.jpg) contains more than it seems.

## Source

[garden](./garden.jpg) (JPEG Image)

# Solution

In this challenge, we are given a JPEG image. Like every other binary file we get, we can check if the flag is written in plain text using the [strings](https://linux.die.net/man/1/strings) and [grep](https://linux.die.net/man/1/grep) commands:

```bash
$ strings garden.jpg | grep pico
Here is a flag "picoCTF{more_than_m33ts_the_3y33dd2eEF5}"
```

**The Flag:** `picoCTF{more_than_m33ts_the_3y33dd2eEF5}`
