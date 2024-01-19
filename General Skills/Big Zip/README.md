# Big Zip

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 100

# Challenge

## Description

Unzip this archive and find the flag.
- [Download zip file](./big-zip-files.zip)

## Source

[big-zip-files.zip](./big-zip-files.zip) (ZIP archive)

# Solution

After unzipping the archive, we get a large hierarchy of directories and files. We need to find the flag. We can use the `grep -r` command to search for a string recursively in all of the files:

```bash
$ grep -r picoCTF big-zip-files
big-zip-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```

**The Flag:** `picoCTF{gr3p_15_m4g1c_ef8790dc}`
