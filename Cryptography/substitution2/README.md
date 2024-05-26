# substitution2

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Cryptography  
**Points:** 100

# Challenge

## Description

It seems that another encrypted message has been intercepted. The encryptor seems to have learned their lesson though and now there isn't any punctuation! Can you still crack the cipher?  
Download the message [here](./message.txt).

## Source

[message.txt](./message.txt) (Text file)

# Solution

This challenge is similar to the [previous one](../substitution1/README.md), but this time the message is without punctuation. Although it is harder to decrypt, it is still possible, using the same methods as before.

After analyzing the message, we get the following recipe:

```
Substitute('ABCDEFGHIJKLMNOPQRSTUVWXYZ','u.wrgtnbqecfohkvi.sympladx',true)
```

And it gives us the decrypted message, which includes the flag.

**The Flag:** `picoCTF{N6R4M_4N41Y515_15_73D10U5_42EA1770}`
