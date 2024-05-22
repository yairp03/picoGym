# vault-door-8

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 450

# Challenge

## Description

Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: [VaultDoor8.java](./VaultDoor8.java)

## Source

[VaultDoor8.java](./VaultDoor8.java) (Java source)

# Solution

For starters, the source code is a mess. We can fix that by formatting the code using an IDE or an online formatter. Now we can see that the code is taking every character in the password, and switch bits withing the ASCII value of the character. We can write a similar code in [python](./solve.py) to reverse the process and get the flag:

```python
from pathlib import Path


def parse_values_from_line(line: str) -> list[int]:
    return [
        int(v.strip()[:4], 16) for v in line.split(", ") if v.strip().startswith("0x")
    ]


def shift_left(value: int, amount: int) -> int:
    if amount < 0:
        return shift_right(value, -amount)
    return value << amount


def shift_right(value: int, amount: int) -> int:
    if amount < 0:
        return shift_left(value, -amount)
    return value >> amount


def switch_bits(char: int, pos1: int, pos2: int) -> int:
    mask1 = 1 << pos1
    mask2 = 1 << pos2
    bit1 = char & mask1
    bit2 = char & mask2
    rest = char & ~(mask1 | mask2)
    shift = pos2 - pos1
    return shift_left(bit1, shift) | shift_right(bit2, shift) | rest


def unscramble(scrambled: list[int]) -> str:
    result = ""
    for char in scrambled:
        # Switching the bits in reversed order
        char = switch_bits(char, 6, 7)
        char = switch_bits(char, 2, 5)
        char = switch_bits(char, 3, 4)
        char = switch_bits(char, 0, 1)
        char = switch_bits(char, 4, 7)
        char = switch_bits(char, 5, 6)
        char = switch_bits(char, 0, 3)
        char = switch_bits(char, 2, 1)
        result += chr(char)
    return result


with Path("./VaultDoor8.java").open() as java_file:
    values_lines = java_file.readlines()[62:64]

values = []
for line in values_lines:
    values.extend(parse_values_from_line(line))

password = unscramble(values)

print(f"Flag is: picoCTF{{{password}}}")
```

Running the script will give us the flag:

```bash
$ python3 solve.py
Flag is: picoCTF{s0m3_m0r3_b1t_sh1fTiNg_91c642112}
```

**The Flag:** `picoCTF{s0m3_m0r3_b1t_sh1fTiNg_91c642112}`
