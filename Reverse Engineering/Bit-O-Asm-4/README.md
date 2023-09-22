# Bit-O-Asm-1

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.  
Download the assembly dump [here](./disassembler-dump0_d.txt).

## Source

[disassembler-dump0_d.txt](./disassembler-dump0_d.txt) (Assembly dump)

# Solution

Here we get an assembly dump, and we need to figure out the value of `eax` at the end of the program. This assembly represents a program with a simple comparison. It starts at `<+22>` where the value stored in `DWORD PTR [rbp-0x4]`, which is `0x9fe1a` (`<+15>`) is being compared to `0x2710`, and if it is smaller or equal, the program jumps to `<+37>`. That's not the case here, so the program continues regularly and proceeds to `<+31>`, where the value in `DWORD PTR [rbp-0x4]` (`0x9fe1a`) is being subtracted with `0x65`. Then, at `<+35>`, the program jumps unconditionally to `<+41>`, where `eax` is set to the value in `DWORD PTR [rbp-0x4]`, and the program ends. The value there is `0x9fe1a - 0x65`. We can calculate the result using a calculator that supports hex numbers, like Windows' calculator, or we can use python:

```python
> 0x9fe1a - 0x65
654773
```

**The Flag:** `picoCTF{654773}`
