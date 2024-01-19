# what's a net cat?

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills
**Points:** 100

# Challenge

## Description

Using netcat (nc) is going to be pretty important. Can you connect to `jupiter.challenges.picoctf.org` at port `41120` to get the flag?

**Solve this problem using Python pwntools.**

# Solution

As suggested, we'll use pwntools to solve this challenge. First, we'll import the `pwn` module, and connect to the server:

```python
from pwn import *

conn = remote('jupiter.challenges.picoctf.org', 41120)
conn.interactive()
```

Now let's run the script:

```
$ python3 solve.py
...
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_3214be47}
...
```

Right after connecting, the server sends us the flag. We can also parse the output to get only the flag:

```python
from pwn import *

conn = remote('jupiter.challenges.picoctf.org', 41120)
content = conn.recvuntil(b'}').decode()
flag = content[content.find('picoCTF{'):]

print('Flag: ' + flag)
```

```
$ python3 solve.py
...
Flag: picoCTF{nEtCat_Mast3ry_3214be47}
...
```

**The Flag:** `picoCTF{nEtCat_Mast3ry_3214be47}`
