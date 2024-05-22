# vault-door-7

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 400

# Challenge

## Description

This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: [VaultDoor7.java](./VaultDoor7.java)

## Source

[VaultDoor7.java](./VaultDoor7.java) (Java source)

# Solution

In this challenge, the 32 characters of the password are packed into 8 integers, each containing 4 characters. The characters are packed into the integers using bit shifts. We can reverse this process by unpacking the characters from the integers using bit shifts. We can do this using the following [python script](./solve.py):

```python
from pathlib import Path


def unpack_number(number: int) -> str:
    return number.to_bytes(4).decode()


with Path("./VaultDoor7.java").open() as java_file:
    numbers_lines = java_file.readlines()[57:65]

numbers = []
before_number = "== "
for line in numbers_lines:
    number_index = line.index(before_number) + len(before_number)
    numbers.append(int(line[number_index:].strip(";\n")))

password = ""
for number in numbers:
    password += unpack_number(number)

print(f"Flag is: picoCTF{{{password}}}")
```

Running the script will give us the flag:

```bash
$ python3 solve.py
Flag is: picoCTF{A_b1t_0f_b1t_sh1fTiNg_702640db5a}
```

**The Flag:** `picoCTF{A_b1t_0f_b1t_sh1fTiNg_702640db5a}`
