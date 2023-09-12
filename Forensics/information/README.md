# information

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Forensics  
**Points:** 10

# Challenge

## Description

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](./cat.jpg)

## Source

[cat.jpg](./cat.jpg) (JPEG image)

# Solution

In this challenge, we are given an image. A useful tool when dealing with images, called [exiftool](/Guides/Tools/exiftool.md), and it can be used to extract metadata from images.

Let's run it on our image:

```bash
$ exiftool cat.jpg
ExifTool Version Number         : 12.40
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 KiB
File Modification Date/Time     : 2021:03:15 18:24:46+00:00
File Access Date/Time           : 2022:07:04 10:47:44+00:00
File Inode Change Date/Time     : 2022:07:04 10:47:37+00:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

One thing that stands out is the `License` field, which instead of containing a normal textual license, it contains a string that looks `base64` encoded. We can decode it in multiple ways, here are some of them:

## Solution 1

Use [CyberChef](/Guides/Tools/CyberChef.md) with [this recipe](<https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)>):

```
From_Base64('A-Za-z0-9+/=',true,false)
```

## Solution 2

Use python's builtin [base64](https://docs.python.org/3/library/base64.html) library:

```py
import base64

encoded_flag = 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'
flag = base64.b64decode(encoded_flag).decode()

print(flag)
```

```
picoCTF{the_m3tadata_1s_modified}
```

**The Flag:** `picoCTF{the_m3tadata_1s_modified}`
