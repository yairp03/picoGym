# crackme-py

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 30

# Challenge

## Description

[crackme.py](./crackme.py)

## Source

[crackme.py](./crackme.py) (Python script)

# Solution

In this challenge we get a Python script that has two functions, one that called `choose_greatest` which is not very interesting, and one that called `decode_secret`. Also, it has a global variable called `bezos_cc_secret` which is probably the encoded flag.
We can trigger the `decode_secret` function with the global secret by modifing the code:

```python
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE067d3eh2bN"

def decode_secret(secret):
    ...

def choose_greatest():
    ...

# choose_greatest()
decode_secret(bezos_cc_secret)
```

And run it:

```bash
$ python3 crackme.py
picoCTF{1|\/|_4_p34|\|ut_ef5b69a3}
```

**The Flag:** `picoCTF{1|\/|_4_p34|\|ut_ef5b69a3}`
