# vault-door-4

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 250

# Challenge

## Description

This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](./VaultDoor4.java)

## Source

[VaultDoor4.java](./VaultDoor4.java) (Java source)

# Solution

This challenge is similar to the previous vault-door challenges, but this time the password is being encoded using ASCII values in different ways. We can scrape the values from the code, and convert each ASCII value to its corresponding character to get the flag. Here is a [python script](./solve.py) that does this:

```python
from pathlib import Path


def parse_items_from_line(line: str) -> list[str]:
    return [v.strip() for v in line.strip().split(",") if v.strip()]


def parse_ascii_with_base(line: str, base: int) -> str:
    values = [chr(int(v, base=base)) for v in parse_items_from_line(line)]
    return "".join(values)


with Path("VaultDoor4.java").open() as java_file:
    lines = java_file.readlines()

decimals_str = parse_ascii_with_base(lines[32], 10)
hexes_str = parse_ascii_with_base(lines[33], 16)
octals_str = parse_ascii_with_base(lines[34], 8)
chars_str = "".join([v[1] for v in parse_items_from_line(lines[35])])

password = decimals_str + hexes_str + octals_str + chars_str

print(f"Flag is: picoCTF{{{password}}}")
```

Running the script will give us the flag:

```bash
$ python3 solve.py
Flag is: picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}
```

**The Flag:** `picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}`
