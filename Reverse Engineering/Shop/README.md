# Shop

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 50

# Challenge

## Description

Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](./source). The shop is open for business at `nc mercury.picoctf.net 11371`.

## Source

[source](./source) (32-bit ELF)

# Solution

Let's connect to the server:

```bash
$ nc mercury.picoctf.net 11371
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option:
```

We don't have enough money to buy the flag, but we can buy another item:

```
Choose an option:
0
How many do you want to buy?
```

We can choose how much quiches we want, but we don't have much to do with them. We can see that if we enter a negative number, it still works:

```
How many do you want to buy?
-6
You have 100 coins
        Item            Price   Count
(0) Quiet Quiches       10      18
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option:
```

Seems like when we bought a negative number of items, we got more coins! Now we have enough to buy the flag:

```
Choose an option: 
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 98 56 100 55 50 55 49 102 125]
```

We can decode the flag using the same methods as in [Nice netcat](../../General%20Skills/Nice%20netcat/README.md) challenge, and we get the flag.

**The Flag:** `picoCTF{b4d_brogrammer_b8d7271f}`
