# interencdec

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Cryptography  
**Points:** 50

# Challenge

## Description

Can you get the real meaning from this file.  
Download the file [here](./enc_flag).

## Source

[enc_flag](./enc_flag) (ASCII text)

# Solution

Here we get a file named `enc_flag`, that by the name seems to be an encrypted flag. Let's start by looking at the contents of the file:

```bash
$ cat enc_flag
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg==
```

The contents of the file ends with some equal signs, which is a common indicator for base64 encoding. We can decode the contents of the file using the `base64` command:

```bash
$ cat enc_flag | base64 -d
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ=='
```

Another base64 encoded string. Let's decode this one too. Before we decode it, we need to remove the `b'` and `'` characters from the string. We can do this by using the `cut` command:

```bash
$ cat enc_flag | base64 -d | cut -d "'" -f 2 | base64 -d
wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}
```

The parameters for the `cut` command are `-d "'"` to specify the delimiter as `'` and `-f 2` to get the second field. The result is seems to be encoded with a Caesar cipher. We can decode it using the `tr` command. We can see that the first `w` should be `p`, so we can build the translation by it:

```bash
$ cat enc_flag | base64 -d | cut -d "'" -f 2 | base64 -d | tr 'w-za-vW-ZA-V' 'p-za-oP-ZA-O'
picoCTF{caesar_d3cr9pt3d_890d2379}
```

**The Flag:** `picoCTF{caesar_d3cr9pt3d_890d2379}`
