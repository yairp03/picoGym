enc = input()

a = []
for c in enc:
    c1 = ord(c) >> 8
    c2 = ord(c) & 0xFF
    a.append(chr(c1))
    a.append(chr(c2))

flag = ''.join(a)
print(flag)
