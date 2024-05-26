# Super SSH

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 25

# Challenge

## Description

Using a Secure Shell (SSH) is going to be pretty important.  
Can you `ssh` as `ctf-player` to `titan.picoctf.net` at port `52721` to get the flag?  
You'll also need the password `6dd28e9b`. If asked, accept the fingerprint with `yes`.  
If your device doesn't have a shell, you can use: https://webshell.picoctf.org  
If you're not sure what a shell is, check out our Primer: https://primer.picoctf.com/#_the_shell

# Solution

This challenge is a simple SSH challenge. We can use the provided credentials to SSH into the server and get the flag.

```
$ ssh -p 52721 ctf-player@titan.picoctf.net
...
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
...
ctf-player@titan-picoctf.net's password: 6dd28e9b
Welcome ctf-player, here's your flag: picoCTF{s3cur3_c0nn3ct10n_5d09a462}
```

**The Flag:** `picoCTF{s3cur3_c0nn3ct10n_5d09a462}`
