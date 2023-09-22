# GDB baby step 3

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

Now for something a little different. `0x2262c96b` is loaded into memory in the `main` function. Examine byte-wise the memory that the constant is loaded in by using the GDB command `x/4xb addr`. The flag is the four bytes as they are stored in memory. If you find the bytes `0x11 0x22 0x33 0x44` in the memory location, your flag would be: `picoCTF{0x11223344}`.
Debug [this](./debugger0_c).

## Source

[debugger0_c](./debugger0_c) (ELF 64-bit)

# Solution

Same as last challenge:

```bash
$ chmod +x ./debugger0_c
$ gdb ./debugger0_c
(gdb) set disassembly-flavor intel
(gdb) disas main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x2262c96b
   0x000000000040111c <+22>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040111f <+25>:    pop    rbp
   0x0000000000401120 <+26>:    ret
End of assembler dump.
```

We need to examine the memory at `[rbp-0x4]` after the constant `0x2262c96b` is written, so we can set a breakpoint at `<+22>` and examine the memory there using the `x/4xb` command:

```bash
(gdb) b *main+22
Breakpoint 1 at 0x40111c
(gdb) r
...
Breakpoint 1, 0x000000000040111c in main ()
(gdb) x/4xb $rbp-0x4
0x7fffffffd97c: 0x6b    0xc9    0x62    0x22
```

Note that `x` is the name of the command that examines memory, `4` is the number of units to examine, `x` is the display format (hex), and `b` is the unit size (bytes).

**The Flag:** `picoCTF{0x6bc96222}`
