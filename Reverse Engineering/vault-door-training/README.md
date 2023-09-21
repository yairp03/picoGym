# vault-door-training

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 50

# Challenge

## Description

Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](./VaultDoorTraining.java)

## Source

[VaultDoorTraining.java](./VaultDoorTraining.java) (Java source)

# Solution

In this challenge, we get a java source file. Opening and reading it, we can see that it's a simple string comparison, and the password, which is the flag, is written plainly in the source code:

```java
public boolean checkPassword(String password) {
    return password.equals("w4rm1ng_Up_w1tH_jAv4_3808d338b46");
}
```

Wrapping the password with `picoCTF{}` gives us the flag.

**The Flag:** `picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46}`
