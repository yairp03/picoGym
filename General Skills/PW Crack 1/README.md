# PW Crack 1

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 100

# Challenge

## Description

Can you crack the password to get the flag?  
Download the password checker [here](./level1.py) and you'll need the encrypted [flag](./level1.flag.txt.enc) in the same directory too.

## Source

[level1.py](./level1.py) (Python script)  
[level1.flag.txt.enc](./level1.flag.txt.enc) (data file)

# Solution

Running the script, we see that it asks for a password and then checks if it's correct:

```
$ python3 level1.py
Please enter correct password for flag: 1234
That password is incorrect
```

Let's take a look at the code:

```python
# ...
user_pw = input("Please enter correct password for flag: ")
if( user_pw == "691d"):
    print("Welcome back... your flag, user:")
# ...
```

So the password is `691d`. Let's try it:

```
$ python3 level1.py
Please enter correct password for flag: 691d
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_56891419}
```

**The Flag:** `picoCTF{545h_r1ng1ng_56891419}`
