from pwn import *

KEY_LEN = 50000

# Connect to challenge server
conn = connect('mercury.picoctf.net', 58913)

# Get encrypted flag
conn.recvuntil(b'This is the encrypted flag!\n')
encrypted_flag = bytes.fromhex(conn.recvline().decode().strip())
flag_len = len(encrypted_flag)

# Reset key to the start
conn.recvuntil(b'What data would you like to encrypt? ')
conn.sendline(b'A' * (KEY_LEN - flag_len))

# Decrypt flag
conn.recvuntil(b'What data would you like to encrypt? ')
conn.sendline(encrypted_flag)
conn.recvuntil(b'Here ya go!\n')
flag = bytes.fromhex(conn.recvline().decode().strip()).decode()

print(f'Flag is: picoCTF{{{flag}}}')
