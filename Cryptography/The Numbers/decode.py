ENCODED_FLAG = '16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }'

result = ''
for n in ENCODED_FLAG.split():
    if n.isdigit():
        result += chr(int(n) + ord('A') - 1)
    else:
        result += n

print('Flag:', result)
