# Bit-O-Asm-1

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.  
Download the assembly dump [here](./disassembler-dump0_c.txt).

## Source

[disassembler-dump0_c.txt](./disassembler-dump0_c.txt) (Assembly dump)

# Solution

Here we get an assembly dump, and we need to figure out the value of `eax` at the end of the program. `eax` first changes at `<+29>` and it is set to `DWORD PTR [rbp-0xc]`, which is equal, according to the instruction at `<+15>`, to `0x9fe1a`. Then, at `<+32>`, `eax` is is multiplied by `DWORD PTR [rbp-0x8]`, which is equal to `0x4` (according to the instruction at `<+22>`). Finally, at `<+36>`, the result is being added with `0x1f5`, and stored back in `eax`.

We can calculate the result using a calculator that supports hex numbers, like Windows' calculator, or we can use python:

```python
> 0x9fe1a * 0x4 + 0x1f5
2619997
```

The instructions at `<+41>` and `<+44>` are not relevant, because they don't actually change `eax`, so the result is `2619997`, and the flag is `picoCTF{2619997}`.

**The Flag:** `picoCTF{2619997}`
