# Magikarp Ground Mission

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 30

# Challenge

## Description

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `481e7b14`

## Challenge Endpoints

**SSH** ssh ctf-player@venus.picoctf.net -p 55862

# Solution

Let's follow the instructions and connect to the server via `SSH`:

```bash
$ ssh ctf-player@venus.picoctf.net -p 55862
ctf-player@venus.picoctf.net's password: 481e7b14
ctf-player@pico-chall$
```

From now on, it's just a matter of following the instructions using the following commands:

```
ls - list directory contents
cat - print file contents
cd - change directory
```

```bash
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt

ctf-player@pico-chall$ cat 1of3.flag.txt
picoCTF{xxsh_

ctf-player@pico-chall$ cat instructions-to-2of3.txt
Next, go to the root of all things, more succinctly `/`

ctf-player@pico-chall$ cd /
ctf-player@pico-chall$ ls
2of3.flag.txt  bin  boot  dev  etc  home  instructions-to-3of3.txt  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

ctf-player@pico-chall$ cat 2of3.flag.txt
0ut_0f_\/\/4t3r_

ctf-player@pico-chall$ cat instructions-to-3of3.txt
Lastly, ctf-player, go home... more succinctly `~`

ctf-player@pico-chall$ cd ~
ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in

ctf-player@pico-chall$ cat 3of3.flag.txt
1118a9a4}
```

Concatenate the three parts and we get the flag.

**The Flag:** `picoCTF{xxsh_0ut_0f_\/\/4t3r_1118a9a4}`
