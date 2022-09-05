flag = '********'

a = []
for i in range(0, len(flag), 2):
    b = (ord(flag[i]) << 8) + ord(flag[i + 1])
    a.append(chr(b))

enc = ''.join(a)
