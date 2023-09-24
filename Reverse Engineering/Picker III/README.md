# Picker III

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

Can you figure out how this program works to get the flag?
Connect to the program with netcat:
`$ nc saturn.picoctf.net 61303`
The program's source code can be downloaded [here](./picker-III.py).

## Source

[picker-III.py](./picker-III.py) (Python script)

# Solution

Here we get the python script from the [previous challenge](../Picker%20II/README.md) with a few modifications. Now we are limited to run functions only from a functions table, by entering their index. The functions table is a string of 4 functions, where each functions is 32 chars long, padded with spaces.

One of the functions is `write_variable` which allows us to change the value of a global variable. We can use this function to change to value of the table, so it will contain the function `win`, which prints the flag. While doing so, we need to make sure that the table size remains the same, as the program checks it before using the table.

We can enter the new table manually, but it's easier and less error prone to do it using a script, I'll use python with [pwntools](/Guides/Tools/pwntools.md):

```python
from pwn import *

NEW_TABLE = 'win'.ljust(32, ' ') + ('A' * 32) * 3

# Make the connection
conn = remote('saturn.picoctf.net', 61303)

# Invoke write_variable()
conn.sendlineafter(b'==> ', b'3')

# Write new table
conn.sendlineafter(b'write: ', b'func_table') # Variable name
conn.sendlineafter(b'variable: ', f'"{NEW_TABLE}"'.encode()) # Variable value

# Invoke first table's function (win())
conn.sendlineafter(b'==> ', b'1')
flag = conn.recvline(False).decode()

print('Flag:', flag)
```

```
Flag: 0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x63 0x32 0x30 0x66 0x35 0x32 0x32 0x32 0x7d
```

The flag is encoded in hex, we can decode it the same way as in [ASCII Numbers](../../General%20Skills/ASCII%20Numbers/README.md) challenge and we get the flag:

```
picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_c20f5222}
```

**The Flag:** `picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_c20f5222}`
