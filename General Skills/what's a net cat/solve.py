from pwn import *

conn = remote('jupiter.challenges.picoctf.org', 41120)
content = conn.recvuntil(b'}').decode()
flag = content[content.find('picoCTF{'):]

print('Flag: ' + flag)
