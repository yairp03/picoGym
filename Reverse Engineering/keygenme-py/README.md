# keygenme-py

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 30

# Challenge

## Description

[keygenme-trial.py](./keygenme-trial.py)

## Source

[keygenme-trial.py](./keygenme-trial.py) (Python script)

# Solution

In this challenge, we are given a trial version of a `keygenme` program. The program lets you enter a license key to get the full version, and that key is also seems to be flag.
Looking at the code that checks the license key, we can see that the key is constructed from static parts, and a dynamic part that is calculated according to the username, in this case is `FREEMAN`. We can run the same logic on our own, and get the license key/flag:

```python
import hashlib

def get_dynamic_part(username: bytes) -> str:
    sha = hashlib.sha256(username).hexdigest()
    return ''.join([sha[4], sha[5], sha[3], sha[6], sha[2], sha[7], sha[1], sha[8]])

print(f'picoCTF{{1n_7h3_|<3y_of_{get_dynamic_part(b"FREEMAN")}}}')
```

```bash
$ python ./script.py
picoCTF{1n_7h3_|<3y_of_0d208392}
```

We can check that the flag is correct by running the program with the flag as the license key:

```
$ python ./keygenme-trial.py
Menu:
...
(c) Enter License Key
...
What would you like to do, FREEMAN (a/b/c/d)? c
Enter your license key: picoCTF{1n_7h3_|<3y_of_0d208392}

Full version written to 'keygenme.py'.

Exiting trial version...

...
```

And we got the confirmation that the flag is indeed correct.

**The Flag:** `picoCTF{1n_7h3_|<3y_of_0d208392}`
