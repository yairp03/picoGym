# GDB baby step 2

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 100

# Challenge

## Description

Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.  
Debug [this](./debugger0_b).

## Source

[debugger0_b](./debugger0_b) (ELF 64-bit)

# Solution

Here we get an executable, let's ensure it's execution permissions and run it with gdb:

```bash
$ chmod +x ./debugger0_b
$ gdb ./debugger0_b
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
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x1e0da
   0x000000000040111c <+22>:    mov    DWORD PTR [rbp-0xc],0x25f
   0x0000000000401123 <+29>:    mov    DWORD PTR [rbp-0x8],0x0
   0x000000000040112a <+36>:    jmp    0x401136 <main+48>
   0x000000000040112c <+38>:    mov    eax,DWORD PTR [rbp-0x8]
   0x000000000040112f <+41>:    add    DWORD PTR [rbp-0x4],eax
   0x0000000000401132 <+44>:    add    DWORD PTR [rbp-0x8],0x1
   0x0000000000401136 <+48>:    mov    eax,DWORD PTR [rbp-0x8]
   0x0000000000401139 <+51>:    cmp    eax,DWORD PTR [rbp-0xc]
   0x000000000040113c <+54>:    jl     0x40112c <main+38>
   0x000000000040113e <+56>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401141 <+59>:    pop    rbp
   0x0000000000401142 <+60>:    ret
End of assembler dump.
```

We see that lines `<+38>` to `<+54>` are a loop. We can statically analyze the code and calculate by hand the value of `eax` at the end of the loop, but we can also use gdb to do it for us.

The way to do it is to set a breakpoint at the end of the loop, using the `b` (short for `break`) command, and then run the program using the `r` (short for `run`) command. When the breakpoint is reached, we can use the `i r` (short for `info registers`) command to see the value of `eax`:

```bash
(gdb) b *main+59
Breakpoint 1 at 0x401141
(gdb) r
...
Breakpoint 1, 0x0000000000401141 in main ()
(gdb) i r eax
eax            0x4af4b             307019
```

The value of `eax` at the end of the program is `307019` so the flag is `picoCTF{307019}`.

**The Flag:** `picoCTF{307019}`
