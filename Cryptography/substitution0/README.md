# substitution0

**Author:** [yairp03](https://github.com/yairp03)  
**Category:** Cryptography  
**Points:** 100

# Challenge

## Description

A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?  
Download the message [here](./message.txt).

## Source

[message.txt](./message.txt) (Text file)

# Solution

As the challenge hints, the message is encrypted using a substitution cipher, and the key is given at the beginning of the message. We can decrypt the message using a simple [Python script](./solve.py):

```python
import os
import string
from pathlib import Path

# Parse the key and the message
message_content = Path("./message.txt").read_text()
substitution_chars, encrypted_message = message_content.split(os.linesep * 2, maxsplit=1)

# Create the cipher
cipher = str.maketrans(
    substitution_chars.strip().lower() + substitution_chars.strip().upper(),
    string.ascii_lowercase + string.ascii_uppercase,
)

# Decrypt
decrypted_message = encrypted_message.translate(cipher)
print(decrypted_message)
```

Running the script will output the following:

```bash
$ python3 solve.py
Hereupon Legrand arose, with a grave and stately air, and brought me the beetle
from a glass case in which it was enclosed. It was a beautiful scarabaeus, and, at
that time, unknown to naturalists—of course a great prize in a scientific point
of view. There were two round black spots near one extremity of the back, and a
long one near the other. The scales were exceedingly hard and glossy, with all the
appearance of burnished gold. The weight of the insect was very remarkable, and,
taking all things into consideration, I could hardly blame Jupiter for his opinion
respecting it.

The flag is: picoCTF{5UB5717U710N_3V0LU710N_59533A2E}
```

**The Flag:** `picoCTF{5UB5717U710N_3V0LU710N_59533A2E}`
