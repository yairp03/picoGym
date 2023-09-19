# ARMssembly 0

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Reverse Engineering  
**Points:** 40

# Challenge

## Description

What integer does this program print with arguments `4134207980` and `950176538`? File: [chall.S](./chall.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Source

[chall.S](./chall.S) (ARM assembly code)

# Solution

Here, we get an assembly code, that, according to the description, takes two arguments and prints an integer. We can find a way to assemble and run the code, but it's a great opportunity to learn how to read assembly code, especially assembly code written in ARM.  
On the top of the file, we can see that the assembly code is written for the ARMv8-A architecture, so to learn how to read it, we can look up online for ARMv8-A sources. I found these two sources to be very helpful:

- [ARMv8 A64 Quick Reference](https://courses.cs.washington.edu/courses/cse469/18wi/Materials/arm64.pdf)
- [Overview of ARM64 ABI conventions](https://learn.microsoft.com/en-us/cpp/build/arm64-windows-abi-conventions)

Let's start by looking at the `func1` function.

```arm
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #16     // Creates a stack frame
	str	w0, [sp, 12]
	str	w1, [sp, 8]
	ldr	w1, [sp, 12]
	ldr	w0, [sp, 8]
	cmp	w1, w0
	bls	.L2
	ldr	w0, [sp, 12]
	b	.L3
.L2:
	ldr	w0, [sp, 8]
.L3:
	add	sp, sp, 16      // Destroys the stack frame
	ret
	.size	func1, .-func1
	.section	.rodata
```

We can see that the first four lines (after the stack frame creation), just replaces the two arguments given to the function in the registers `w0` and `w1`. Then, if `w1` isn't less than or equal to `w0`, meaning it is greater than `w1`, the function returns the value stored in `[sp, 12]`, which is the value that currently stored in `w1`. Otherwise, it returns the value stored in `[sp, 8]`, which is the value that currently stored in `w0`. With this logic, we can see that the function returns the maximum value between the two arguments.

Now, let's look at the `main` function.

```arm
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	x19, [sp, 16]
	str	w0, [x29, 44]
	str	x1, [x29, 32]

	ldr	x0, [x29, 32]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi

	mov	w19, w0
	ldr	x0, [x29, 32]
	add	x0, x0, 16
	ldr	x0, [x0]
	bl	atoi

	mov	w1, w0
	mov	w0, w19
	bl	func1

	mov	w1, w0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf

	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```

I divided the function into sections to make it more readable. The first part does some initialization, not really important. Then, we can see two calls to `atoi`, which converts the string arguments to integers. Then, we can see a call to `func1`, which we already know returns the maximum value between the two arguments. Finally, we can see a call to `printf`, which prints the result.

So, to get the flag, we need to find the maximum value between the two values we got in the challenge description. In this case, the maximum value is `4134207980`, so, using python, we can get the flag:

```python
> f"picoCTF{{{hex(4134207980)[2:].rjust(8, '0')}}}"
'picoCTF{f66b01ec}'
```

**The Flag:** `picoCTF{f66b01ec}`
