# Bit-O-Asm-1

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.  
Download the assembly dump [here](./disassembler-dump0_a.txt).

## Source

[disassembler-dump0_a.txt](./disassembler-dump0_a.txt) (Assembly dump)

# Solution

Here we get an assembly dump, and we need to figure out the value of `eax` at the end of the program. Here there's only one instruction that modifies `eax` and it's `mov eax, 0x30` which sets `eax` to `0x30` (48 in decimal), so the flag is `picoCTF{48}`.

**The Flag:** `picoCTF{48}`
