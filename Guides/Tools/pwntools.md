# pwntools

`pwntools` is a python library that helps with binary exploitation. It has many useful functions, such as sending and receiving data from a socket, and packing and unpacking data. It also has many useful tools, such as a shellcraft module that helps with shellcoding, and a disassembly module that helps with disassembling data.

## Installation

The `pwntools` package can be installed using `pip`:

```bash
$ pip install pwntools
```

It is recommended to use it with python 3, and is best supported on 64-bit Ubuntu LTS releases.

For further installation instructions, see the [installation page](https://docs.pwntools.com/en/stable/install.html) in the documentation.

## Usage

To use `pwntools`, import it:

```python
from pwn import *

# Your code here
```

### Useful Functions

#### Sending and Receiving Data

- `remote`: Creates a connection to a remote host.

```python
from pwn import *

conn = remote('challenge.ctf.com', 12345)
```

- `process`: Creates a process and connects to it.

```python
from pwn import *

conn = process('./vuln')
```

These objects have useful functions for sending and receiving data. Some of them are:

##### Sending

- `send`: Sends data to the socket.
- `sendafter`: Sends data to the socket after a certain string is received.
- `sendthen`: Sends data to the socket, and then receives data from the socket until a certain string is received.
- `sendline`: Same as `send`, but adds a newline character at the end.
- `sendlineafter`: Same as `sendafter`, but adds a newline character at the end.
- `sendlinethen`: Same as `sendthen`, but adds a newline character at the end.

##### Receiving

- `recv`: Receives data from the socket.
- `recvuntil`: Receives data from the socket until a certain string is received.
- `recvline`: Receives data from the socket until a newline character is received.
- `recvlines`: Receives data from the socket until a newline character is received, and returns a list of the lines.
- `recvall`: Receives all data from the socket until the socket is closed.

#### Packing and Unpacking Data

- `p8`, `p16`, `p32`, `p64`: Packs an integer into a byte string.
- `u8`, `u16`, `u32`, `u64`: Unpacks a byte string into an integer.

## Further Reading

- [pwntools Documentation](https://docs.pwntools.com/en/stable/)
- [pwntools on GitHub](https://github.com/Gallopsled/pwntools)
