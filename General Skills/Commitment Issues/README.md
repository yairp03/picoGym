# Commitment Issues

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** General Skills  
**Points:** 50

# Challenge

## Description

I accidentally wrote the flag down. Good thing I deleted it!  
You download the challenge files here:

- [challenge.zip](./challenge.zip)

## Source

[challenge.zip](./challenge.zip) (ZIP Archive)

# Solution

Here we get a zip file. Let's start by unzipping it:

```bash
$ unzip challenge.zip
```

We can see that the zip contained one folder named `drop-in`, which has a single file named `message.txt`, and a `.git` folder, meaning it's a git repository. Currently, the `message.txt` file just contains the words `TOP SECRET`. Let's look at the git repo using the `git log` command:

```bash
$ git log
commit 3899edb7f3110d613c72ad40083fd8feeef703d0 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:58 2024 +0000

    remove sensitive info

commit 6603cb4ff0c4ea293798c03a32e0d78d5ab12ca2
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:58 2024 +0000

    create flag
```

We can see that the last commit has the message `remove sensitive info`. Seems like reverting back this commit could give us some interesting information. There are many ways to do so, one of them is to completly delete the commit from the branch with the `git reset --hard` command. We need to go one commit backward so we'll use `HEAD~1` as the parameter to the command:

```bash
$ git reset --hard HEAD~1
HEAD is now at 6603cb4 create flag
```

Now when we open the `message.txt` file, it contains the flag.

**The Flag:** `picoCTF{s@n1t1z3_9539be6b}
`
