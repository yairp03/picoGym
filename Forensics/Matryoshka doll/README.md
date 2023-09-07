# Matryoshka doll

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Forensics  
**Points:** 30

# Challenge

## Description

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](./dolls.jpg)

## Source

[dolls.jpg](./dolls.jpg) (JPEG image)

# Solution

In this challenge we get a JPEG image of a Matryoshka doll. The description hints that there are more dolls inside the image, and we need to find the final one.
The tool [binwalk](https://github.com/ReFirmLabs/binwalk) can help with extracting hidden files. Let's run it (`-e` for extraction):

```bash
$ binwalk -e dolls.jpg
...
base_images/2_c.jpg
...
```

We got another image, of a smaller doll. Let's continue with this process:

```
$ cd _dolls.jpg.extracted/base_images/
$ binwalk -e 2_c.jpg
...
base_images/3_c.jpg
...
$ cd _2_c.jpg.extracted/base_images/
$ binwalk -e 3_c.jpg
...
base_images/4_c.jpg
...
$ cd _3_c.jpg.extracted/base_images/
$ binwalk -e 4_c.jpg
...
flag.txt
...
$ cd _4_c.jpg.extracted
$ cat flag.txt
picoCTF{96fac089316e094d41ea046900197662}
```

**The Flag:** `picoCTF{96fac089316e094d41ea046900197662}`
