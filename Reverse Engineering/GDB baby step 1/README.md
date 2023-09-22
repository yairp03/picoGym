# GDB baby step 1

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.  
Disassemble [this](./debugger0_a).

## Source

[debugger0_a](./debugger0_a) (ELF 64-bit)

# Solution

Here we get an executable, let's ensure it's execution permissions and run it with gdb:

```bash
$ chmod +x ./debugger0_a
$ gdb ./debugger0_a
(gdb)
```

Also, I like to set the disassembly flavor to Intel, so I'll do that now:

```bash
(gdb) set disassembly-flavor intel
```

We can start by disassembling the `main` function, using the `disas main` (short for `disassemble main`) command:

```bash
(gdb) disas main
Dump of assembler code for function main:
   0x0000000000001129 <+0>:     endbr64
   0x000000000000112d <+4>:     push   rbp
   0x000000000000112e <+5>:     mov    rbp,rsp
   0x0000000000001131 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000001134 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000001138 <+15>:    mov    eax,0x86342
   0x000000000000113d <+20>:    pop    rbp
   0x000000000000113e <+21>:    ret
End of assembler dump.
```

We can see that at the end of the code, the value `0x86342` (549698 in decimal) is moved into the `eax` register, so that's our flag.

**The Flag:** `picoCTF{549698}`
