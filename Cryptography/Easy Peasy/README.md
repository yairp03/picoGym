# Easy Peasy

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Cryptography  
**Points:** 40

# Challenge

## Description

A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) `nc mercury.picoctf.net 58913` [otp.py](./otp.py)

## Source

[otp.py](./otp.py) (Python script)

# Solution

Here, we get a python script that encrypts the flag with a one-time pad and prints it. The one-time pad is a stream cipher that uses a random key that is as long as the message. The key is only used once, hence the name. After that, we can enter more strings and the script will continue to encrypt and print them, with the rest of the one-time pad. The exploit here is that the key is not actually a one-time pad, because after the key is entirely used, it restores the key to its original state.

We want to trigger such a state, so we need to send a string that is as long as the key, minus the length of the flag. After that, the key is fully restored, and because the encryption is done with XOR, we can just send back the encrypted flag to get the flag.

We can solve the challenge using [pwntools](/Guides/Tools/pwntools.md):

```python
from pwn import *

KEY_LEN = 50000

# Connect to challenge server
conn = connect('mercury.picoctf.net', 58913)

# Get encrypted flag
conn.recvuntil(b'This is the encrypted flag!\n')
encrypted_flag = bytes.fromhex(conn.recvline().decode().strip())
flag_len = len(encrypted_flag)

# Reset key to the start
conn.recvuntil(b'What data would you like to encrypt? ')
conn.sendline(b'A' * (KEY_LEN - flag_len))

# Decrypt flag
conn.recvuntil(b'What data would you like to encrypt? ')
conn.sendline(encrypted_flag)
conn.recvuntil(b'Here ya go!\n')
flag = bytes.fromhex(conn.recvline().decode().strip()).decode()

print(f'Flag is: picoCTF{{{flag}}}')
```

```
Flag is: picoCTF{35ecb423b3b43472c35cc2f41011c6d2}
```

**The Flag:** `picoCTF{35ecb423b3b43472c35cc2f41011c6d2}`
