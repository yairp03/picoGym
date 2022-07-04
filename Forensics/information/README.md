# information
**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Forensics  
**Points:**  10

# Challenge
## Description
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](./cat.jpg)
## Source
[cat.jpg](./cat.jpg) (JPEG image)

# Solution
Giving an image, let's start by running [exiftool](https://linux.die.net/man/1/exiftool) to see the metadata of the image:
```sh
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
We can see the license is a base64 encoded string so let's decode it.
## Solution 1
Use [this cyberchef recipe](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)):
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

**The Flag:** `picoCTF{the_m3tadata_1s_modified}`
