# Bit-O-Asm-1

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.  
Download the assembly dump [here](./disassembler-dump0_b.txt).

## Source

[disassembler-dump0_b.txt](./disassembler-dump0_b.txt) (Assembly dump)

# Solution

Here we get an assembly dump, and we need to figure out the value of `eax` at the end of the program. The last (and only) instruction that modifies `eax` it's `mov eax, DWORD PTR [rpb-0x4]`, so `eax` sets to the value that stored in `[rbp-0x4]`, which is set, just before, to `0x9fe1a`. This number in decimal is equal to `654874`, so the flag is `picoCTF{654874}`.

**The Flag:** `picoCTF{654874}`
