# PW Crack 2

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 100

# Challenge

## Description

Can you crack the password to get the flag?  
Download the password checker [here](./level2.py) and you'll need the encrypted [flag](./level2.flag.txt.enc) in the same directory too.

## Source

[level2.py](./level2.py) (Python script)  
[level2.flag.txt.enc](./level2.flag.txt.enc) (data file)

# Solution

Running the script, we see that it asks for a password and then checks if it's correct:

```
$ python3 level2.py
Please enter correct password for flag: 1234
That password is incorrect
```

Let's take a look at the code:

```python
# ...
user_pw = input("Please enter correct password for flag: ")
if( user_pw == chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65) ):
    print("Welcome back... your flag, user:")
# ...
```

So the password is the result of the expression `chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65)`. Let's run it in the Python interpreter:

```python
$ python3
>>> chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65)
'39ce'
```

So the password is `39ce`. Let's try it:

```
$ python3 level2.py
Please enter correct password for flag: 39ce
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_502ec42e}
```

**The Flag:** `picoCTF{tr45h_51ng1ng_502ec42e}`
