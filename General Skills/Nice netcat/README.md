# Nice netcat...

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 15

# Challenge

## Description

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 22342`, but it doesn't speak English...

# Solution

Let's run this [netcat](https://linux.die.net/man/1/nc) command:

```sh
$ nc mercury.picoctf.net 22342
112
105
99
111
67
84
70
123
103
48
48
100
95
107
49
116
116
121
33
95
110
49
99
51
95
107
49
116
116
121
33
95
53
102
98
53
101
53
49
100
125
10
```

We got a bunch of numbers, and it looks like they are decimal values of ASCII characters. We can convert them to ASCII in multiple ways.

## Solution 1:

Use [this cyberchef recipe](<https://gchq.github.io/CyberChef/#recipe=From_Decimal('Space',false)>):

```
From_Decimal('Space',false)
```

## Solution 2:

Using [this python script](./script.py):

```py
result = ''

while True:
    try:
        num = int(input())
        result += chr(num)
    except:
        break

print(result)
```

We can use [pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html) to run the script:

```sh
$ nc mercury.picoctf.net 22342 | python3 script.py
picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}
```

**The Flag:** `picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}`
