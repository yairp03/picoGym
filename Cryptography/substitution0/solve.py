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
