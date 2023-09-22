# The Numbers

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Cryptography  
**Points:** 50

# Challenge

## Description

The [numbers](./the_numbers.png)... what do they mean?

## Source

[the_numbers.png](./the_numbers.png) (PNG Image)

# Solution

In this challenge, we get an image containings the following string:

```
16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }
```

We can see that there are curly braces, and 7 numbers before the first one, so we can assume that each number represants a letter and this string is the flag encoded. Also, the numbers are between 1 and 26, so we can assume that they are the letters' position in the alphabet.

Using the following python script, we can decode the flag:

```python
ENCODED_FLAG = '16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }'

result = ''
for n in ENCODED_FLAG.split():
    if n.isdigit():
        result += chr(int(n) + ord('A') - 1)
    else:
        result += n

print('Flag:', result)
```

```
Flag: PICOCTF{THENUMBERSMASON}
```

Note: The hint tells us that the flag is in the format `PICOCTF{}`, so we can guess that all of the letters are capital.

**The Flag:** `PICOCTF{THENUMBERSMASON}`
