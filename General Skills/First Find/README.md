# First Find

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 100

# Challenge

## Description

Unzip this archive and find the file named 'uber-secret.txt'
- [Download zip file](./files.zip)

## Source

[files.zip](./files.zip) (ZIP archive)

# Solution

We got a ZIP archive. Let's unzip it:

```bash
$ unzip files.zip
```

We got a hierarchy of directories and files, and we need to find the file named `uber-secret.txt`. We can use the `find` command to search for it:

```bash
$ find files -name uber-secret.txt
files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

We can use the `cat` command to read the file, but we also can use the `-exec` option of `find` to do it (`find` replaces `{}` with the path of the file it found):

```bash
$ find files/ -name uber-secret.txt -exec cat {} +
picoCTF{f1nd_15_f457_ab443fd1}
```

**The Flag:** `picoCTF{f1nd_15_f457_ab443fd1}`
