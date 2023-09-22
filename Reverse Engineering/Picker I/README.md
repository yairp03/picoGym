# Picker I

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

This service can provide you with a random number, but can it do anything else?  
Connect to the program with netcat:  
`$ nc saturn.picoctf.net 52220`  
The program's source code can be downloaded [here](./picker-I.py).

## Source

[picker-I.py](./picker-I.py) (Python script)

# Solution

Here we get a python script that takes a function name from the user and executes it. Looking at the code, we can see that there's a function called `win` that opens a file called `flag.txt`, encodes it to hex represantation and prints it. Let's connect to the server and invoke this function:

```bash
$ nc saturn.picoctf.net 52220
Try entering "getRandomNumber" without the double quotes...
==> win
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x62 0x35 0x32 0x33 0x62 0x32 0x61 0x31 0x7d
```

We can decode it the same way as in the [ASCII Numbers](../../General%20Skills/ASCII%20Numbers/README.md) challenge, and get the flag.

**The Flag:** `picoCTF{4_d14m0nd_1n_7h3_r0ugh_b523b2a1}`
