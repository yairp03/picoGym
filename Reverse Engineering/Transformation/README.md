# Transformation

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 20

# Challenge

## Description

I wonder what this really is... [enc](./enc)  
`''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

## Source

[enc](./enc) (Unicode text)

# Solution

According to the given file's name - [enc](./enc), we can guess that it has encrypted text, and it was encrypted with the given python script.  
Let's break down this oneliner:

```py
flag = '********'

a = []
for i in range(0, len(flag), 2):
    b = (ord(flag[i]) << 8) + ord(flag[i + 1])
    a.append(chr(b))

enc = ''.join(a)
```

We can see that the script iterates the flag, two characters at a time, and attaches their binary presentation to create a new `Unicode` character.  
Now that we understand this, we can write a script to reverse it:

```py
enc = input()

a = []
for c in enc:
    # Taking the first 8 bits
    c1 = ord(c) >> 8
    # Taking the last 8 bits
    c2 = ord(c) & 0xFF
    a.append(chr(c1))
    a.append(chr(c2))

flag = ''.join(a)
print(flag)
```

Now let's pipe the content of [enc](./enc) into the [decrypter](./decrypt.py):

```bash
$ cat enc | python3 decrypt.py
picoCTF{16_bits_inst34d_of_8_e141a0f7}
```

**The Flag:** `picoCTF{16_bits_inst34d_of_8_e141a0f7}`
