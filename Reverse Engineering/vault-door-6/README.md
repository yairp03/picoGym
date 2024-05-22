# vault-door-6

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 350

# Challenge

## Description

This vault uses an XOR encryption scheme. The source code for this vault is here: [VaultDoor6.java](./VaultDoor6.java)

## Source

[VaultDoor6.java](./VaultDoor6.java) (Java source)

# Solution

In this challenge, the password is encrypted using the XOR operation. The XOR operation is reversible, so we can decrypt the password by XORing it with the same key. We can do this using the following [python script](./solve.py):

```python
from pathlib import Path


def parse_values_from_line(line: str) -> list[str]:
    return [v.strip() for v in line.split(",") if v.strip()]


with Path("./VaultDoor6.java").open() as java_file:
    values_lines = java_file.readlines()[29:33]

values = []
for line in values_lines:
    values.extend([int(v, 16) for v in parse_values_from_line(line)])

password = "".join([chr(v ^ 0x55) for v in values])

print(f"Flag is: picoCTF{{{password}}}")
```

Running the script will give us the flag:

```bash
$ python3 solve.py
Flag is: picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_3ce2919}
```

**The Flag:** `picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_3ce2919}`
