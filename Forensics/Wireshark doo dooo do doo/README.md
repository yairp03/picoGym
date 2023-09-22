# Wireshark doo doooo do doo...

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Forensics  
**Points:** 50

# Challenge

## Description

Can you find the flag? [shark1.pcapng](./shark1.pcapng).

## Source

[shark1.pcapng](./shark1.pcapng) (pcapng capture file)

# Solution

In this challenge we get a capture file, we can open it with [wireshark](/Guides/Tools/Wireshark.md).

We can see that there are a lot of packets, and we need to start filtering them.

Looking at the source and destination addresses of the packets, we can recognize that the computer that captured the packets has the IP address `192.168.38.104`. Also, there are a lot of communication with `192.168.38.103` and `192.168.38.105` that doesn't seem to be relevant, so we can filter it out.

```
Filter: !(ip.addr == 192.168.38.103 || ip.addr == 192.168.38.105)
```

That leaves us with `23` packets. We can add another filter to only show those with actual data:

```
Filter: !(ip.addr == 192.168.38.103 || ip.addr == 192.168.38.105) && tcp.len > 0
```

Now we can see that there are only `4` packets left. Searching them manually, we can see that one of them contains the following string, that looks like it contains the flag:

```
Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}
```

The flag is encoded using [ROT13](https://en.wikipedia.org/wiki/ROT13), we can decode it using python's builtin [codecs](https://docs.python.org/3/library/codecs.html) module:

```python
> import codecs
> codecs.decode("Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}", "rot13")
'The flag is picoCTF{p33kab00_1_s33_u_deadbeef}'
```

**The Flag:** `picoCTF{p33kab00_1_s33_u_deadbeef}`
