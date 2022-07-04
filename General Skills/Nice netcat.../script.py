result = ''

while True:
    try:
        num = int(input())
        result += chr(num)
    except:
        break

print(result)