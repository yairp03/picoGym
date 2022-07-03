# Mod 26
**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Cryptography  
**Points:**  10
# Challenge
## Description
Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_********}`

# Solution
According to the description, the file is encrypted with the [ROT13](https://en.wikipedia.org/wiki/ROT13) cipher, and in order to retrive the flag, we'll have to decrypt it.
## Solution 1:
Use [this CyberChef recipe](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)).
## Solution 2:
Use python's builtin [codecs](https://docs.python.org/3/library/codecs.html) library:
```py
import codecs

encrypted_flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_********}"
flag = codecs.decode(encrypted_flag, 'rot13')

print(flag)
```

**The Flag:** `picoCTF{next_time_I'll_try_2_rounds_of_rot13_********}`
