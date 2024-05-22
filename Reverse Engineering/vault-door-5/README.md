# vault-door-5

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 300

# Challenge

## Description

In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](./VaultDoor5.java)

## Source

[VaultDoor5.java](./VaultDoor5.java) [Java source]

# Solution

In this challenge, the vault password is encoded using the functions `urlEncode` and `base64Encode`. We can create a decode functions for each one of them, and decode back the password. Here is a [python script](./solve.py) that does that:

```python
from base64 import b64decode


def url_decode(encoded: str) -> str:
    result = ""
    # Each character represants by a % sign and 2 hex digits
    for i in range(1, len(encoded), 3):
        result += chr(int(encoded[i : i + 2], 16))
    return result


def base64_decode(encoded: str) -> str:
    return b64decode(encoded.encode()).decode()


result = (
    "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
    + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
    + "JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1"
)

password = url_decode(base64_decode(result))
print(f"Flag is: picoCTF{{{password}}}")
```

Running the script will give us the flag:

```bash
$ python3 solve.py
Flag is: picoCTF{c0nv3rt1ng_fr0m_ba5e_64_84fd5095}
```

**The Flag:** `picoCTF{c0nv3rt1ng_fr0m_ba5e_64_84fd5095}`
