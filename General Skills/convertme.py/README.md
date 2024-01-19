# convertme.py

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 100

# Challenge

## Description

Run the Python script and convert the given number from decimal to binary to get the flag.  
[Download Python script](./convertme.py)

## Source

[convertme.py](./convertme.py) (Python script)

# Solution

Let's start by running the script:

```
$ python3 convertme.py
If 30 is in decimal base, what is it in binary base?
Answer: 
```

The script asks us to convert the number 30 from decimal to binary.

## Solution 1:

We can open a Python interpreter and convert the number using the `bin()` function:

```python
$ python3
> bin(30)
'0b11110'
```

And now enter the answer to the script:

```
If 30 is in decimal base, what is it in binary base?
Answer: 0b11110
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_762f748e}
```

## Solution 2:

After all, we have the script's source code. Let's take a look at it:

```python
num = random.choice(range(10,101))
# ...
ans = input('Answer: ')
# ...
ans_num = int(ans, base=2)
if ans_num == num:
```

The script converts the input to an integer with base 2, and compares it the random number chosen at the beginning. We can modify the script so the condition will always be true:

```python
num = random.choice(range(10,101))
# ...
ans = input('Answer: ')
# ...
ans_num = int(ans, base=2)
if True: # Will always enter the if statement
```

```
python3 convertme.py
If 23 is in decimal base, what is it in binary base?
Answer: 0
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_762f748e}
```

**The Flag:** `picoCTF{4ll_y0ur_b4535_762f748e}`
