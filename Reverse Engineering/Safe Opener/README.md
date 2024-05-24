# Safe Opener

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

Can you open this safe?  
I forgot the key to my safe but this [program](./SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?  
Put the password you recover into the picoCTF flag format like:  
`picoCTF{password}`

## Source

[SafeOpener.java](./SafeOpener.java) (Java source)

# Solution

Looking at the java source, we can see that the program recieves the password (15), encodes it using a base64 encoder (17), and then sends it to the `openSafe()` function, which compares it to a hardcoded base64 string. We can decode this hardcoded string to get the flag. An easy way to do so is with a [python script](./solve.py):

```python
import base64

def base64_decode(encoded: str) -> str:
    return base64.b64decode(encoded.encode()).decode()

encoded_password = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"

print(f"Flag is: picoCTF{{{base64_decode(encoded_password)}}}")
```

Running the script will give us the flag:

```bash
$ python3 solve.py
Flag is: picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
```

**The Flag:** `picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`
