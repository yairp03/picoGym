# vault-door-1

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](./VaultDoor1.java)

## Source

[VaultDoor1.java](./VaultDoor1.java) (Java source)

# Solution

In the [previous challenge](../vault-door-training/README.md), the password was checked using a simple string comparison. In this challenge, the password is checked one character at a time, not in order. We can scrape the password from the code using a simple [python script](./solve.py):

```python
from pathlib import Path

with Path("./VaultDoor1.java").open() as java_file:
    # Lines containing password characters
    password_lines = java_file.readlines()[23:55]

password = [""] * 32  # Password length

for line in password_lines:
    index_start = line.index("(") + 1
    index_end = line.index(")")
    index = int(line[index_start:index_end])

    value_index = line.index("'") + 1
    value = line[value_index]

    password[index] = value

print(f"Flag is: picoCTF{{{''.join(password)}}}")
```

Running the script will output the flag:

```bash
$ python3 solve.py
Flag is: picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_f6daf4}
```

**The Flag:** `picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_f6daf4}`
