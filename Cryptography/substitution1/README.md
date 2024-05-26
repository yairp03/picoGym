# substitution1

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Cryptography  
**Points:** 100

# Challenge

## Description

A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again.
Download the message [here](./message.txt).

## Source

[message.txt](./message.txt) (Text file)

# Solution

This challenge is similar to the [previous one](../substitution0/README.md), except now we don't have the cipher key. In this case, we can start substituting characters manually until we find the correct key. The way I did it was by using [CyberChef](/Guides/Tools/CyberChef.md)'s `Substitute` operation.

I started by substituting the entire alphabet with 26 dots (`.`):

```
Substitute('ABCDEFGHIJKLMNOPQRSTUVWXYZ','..........................',true)
```

Looking carefully, we can see that the message ends with the following string:

```
Ove kwtb qevmsjr, kwj osgx tb: qtlvLKO{OE3AH3ULY_4774LI5_4E3_L001_6J0659OM}
```

In the [previous challenge](../substitution0/README.md), the message ends with `The flag is: picoCTF{...}`. We can assume that the current message ends the same way. That means, we have information about some substitions! Now, our recipe will look like this:

```
Substitute('ABCDEFGHIJKLMNOPQRSTUVWXYZ','.s....a..etc..f.p.li.ohg..',true)
```

The message starts to make more sense now. We can start to read the message, and figure out the rest of the letters. For example, the first sentence looks like this:

```
CTFs (sho.t fo. capt..e the flag) a.e a t.pe of co.p.te. sec..it. co.petitio..
```

We can pretty much guess the rest of the letters, and add letters so it'll make sense:

```
CTFs (short for capture the flag) are a type of computer security competition.
```

After decrypting the entire message, we get the following recipe:

```
Substitute('ABCDEFGHIJKLMNOPQRSTUVWXYZ','.s.wrvauketcb.f.pmlinohgyd',true)
```

We are still missing some letters, and sadly, the flag using one of them. Lets look at the almost decrypted flag:

```
picoCTF{FR3.U3NCY_4774CK5_4R3_C001_6E0659FB}
```

Luckily for us, the flags content usually makes sense. We can guess that the missing letter is `Q`. Now we can decrypt the flag.

Final recipe:

```
Substitute('ABCDEFGHIJKLMNOPQRSTUVWXYZ','qs.wrvauketcb.f.pmlinohgyd',true)
```

**The Flag:** `picoCTF{FR3QU3NCY_4774CK5_4R3_C001_6E0659FB}`
