# vault-door-3

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 200

# Challenge

## Description

This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](./VaultDoor3.java)

## Source

[VaultDoor3.java](./VaultDoor3.java) (Java source)

# Solution

In this challenge, the password is being scrambled using some loops, and then checked against a hardcoded string. We can reverse this process using a [python script](./solve.py):

```python
result_string = "jU5t_a_sna_3lpm12g94c_u_4_m7ra41"

password = [""] * 32  # Password length

for i in range(8):
    password[i] = result_string[i]

for i in range(8, 16):
    password[23 - i] = result_string[i]

for i in range(16, 32, 2):
    password[46 - i] = result_string[i]

for i in range(31, 16, -2):
    password[i] = result_string[i]

print(f"Flag is: picoCTF{{{''.join(password)}}}")s
```

Running the script will give us the flag:

```bash
$ python3 solve.py
Flag is: picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}
```

**The Flag:** `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}`
