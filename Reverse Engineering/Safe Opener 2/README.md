# Safe Opener 2

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

What can you do with this file?  
I forgot the key to my safe but this [file](./SafeOpener.class) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

## Source

[SafeOpener.class](./SafeOpener.class) (Compiled Java Class)

# Solution

In this challenge, we are given a compiled Java class file. We need to decompile the class file to view the source code. We can use an online Java decompiler like [this one](http://www.javadecompilers.com/). After decompiling the class file, we get the [source code](./SafeOpener.java), and after a quick look, we can see that the flag is hardcoded in the code:

```java
public class SafeOpener {
    // ...
    public static boolean openSafe(String password) {
        String encodedkey = "picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_0e57c117}";
        // ...
    }
}
```

**The Flag:** `picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_0e57c117}`
