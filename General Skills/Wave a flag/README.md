# Wave a flag
**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:**  10

# Challenge
## Description
Can you invoke help flags for a tool or binary? [This program](./warm) has extraordinarily helpful information...
## Source
[warm](./warm) (ELF 64-bit)

# Solution
By running the [file](https://linux.die.net/man/1/file) command we see that the file we got is executable:
```sh
$ file warm
warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=b11c22752c901adc13ba1ce86eda9d5516f22763, with debug_info, not stripped
```
Let's check the file permissions by using the [ls](https://linux.die.net/man/1/ls) command with the `-l` flag:
```sh
$ ls -l
-rw-r--r--  1 yair  staff  10936 Jul  4 13:09 warm
```
We see it doesn't have an execute permission, so we can add this with [chmod](https://linux.die.net/man/1/chmod):
```sh
$ chmod +x warm
$ ls -l
-rwxr-xr-x  1 yair  staff  10936 Jul  4 13:09 warm
```
Now we can run the file:
```
$ ./warm
Hello user! Pass me a -h to learn what I can do!
```
Following the instructions:
```sh
$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_d6969390}
```

**The Flag:** `picoCTF{b1scu1ts_4nd_gr4vy_d6969390}`
