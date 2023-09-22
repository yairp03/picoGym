# Picker II

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

Can you figure out how this program works to get the flag?
Connect to the program with netcat:
`$ nc saturn.picoctf.net 59376`
The program's source code can be downloaded [here](./picker-II.py).

## Source

[picker-II.py](./picker-II.py) (Python script)

# Solution

We get the code from the [previous challenge](../Picker%20I/README.md), with a minor change: our input can't have the word `win` in it.

Same as before, our input is concatenated with the strings `()` and passed to `eval()`. Using the char `#` at the end of our input, comments out the added part, so we are not limited to running a function that takes no arguments. With that said, instead of running `win()`, we can just open the flag file and read it by ourselves.

```bash
$ nc saturn.picoctf.net 59376
==> print(open('flag.txt').read()) #
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}
```

**The Flag:** `picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}`
