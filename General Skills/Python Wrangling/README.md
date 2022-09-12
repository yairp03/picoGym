# Python Wrangling

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 10

# Challenge

## Description

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](ende.py) using [this password](./pw.txt) to get [the flag](flag.txt.en)?

## Source

[ende.py](./ende.py) (Python script)  
[pw.txt](./pw.txt) (ASCII text)  
[flag.txt.en](./flag.txt.en) (ASCII text)

# Solution

In this challenge, we are requested to decrypt the encrypted flag using the given python script and password.  
Looking at the script, we see it uses an external library called [cryptography](https://pypi.org/project/cryptography/). Let's install it:

```bash
$ pip3 install cryptography
```

Now we can run the script:

```bash
$ python3 ./ende.py
Usage: ./ende.py (-e/-d) [file]
```

We want to decrypt the flag so we'll choose the `-d` option:

```bash
$ python3 ./ende.py -d flag.txt.en
Please enter the password:
```

The script is requesting a password. Luckily for us, we have the password in the `pw.txt` file. We can enter the password manually or use [pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html):

```bash
$ cat pw.txt | python3 ./ende.py -d flag.txt.en
Please enter the password:picoCTF{4p0110_1n_7h3_h0us3_6008014f}
```

**The Flag:** `picoCTF{4p0110_1n_7h3_h0us3_6008014f}`
