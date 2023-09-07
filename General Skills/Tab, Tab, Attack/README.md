# Tab, Tab, Attack

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 20

# Challenge

## Description

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](./Addadshashanammu.zip)

## Source

[Addadshashanammu.zip](./Addadshashanammu.zip) (ZIP archive)

# Solution

We got a ZIP archive. Let's extract it:

```bash
$ unzip Addadshashanammu.zip
Archive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   ...
   inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
```

The ZIP archive contains a lot of nested directories, with one file at the end of the tree. Writing the command `file` and pressing tab multiple times will autocomplete until the final file:

```bash
$ file Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
...: ELF 64-bit ...
```

That's a executable. Using the same tab trick, we can write `./` and let the terminal autocomplete the path to the file:

```bash
$ ./Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}
```

**The Flag:** `picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}`
