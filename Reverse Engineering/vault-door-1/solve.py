from pathlib import Path

with Path("./VaultDoor1.java").open() as java_file:
    # Lines containing password characters
    password_lines = java_file.readlines()[23:55]

password = [""] * 32  # Password length

for line in password_lines:
    index_start = line.index("(") + 1
    index_end = line.index(")")
    index = int(line[index_start:index_end])

    value_index = line.index("'") + 1
    value = line[value_index]

    password[index] = value

print(f"Flag is: picoCTF{{{''.join(password)}}}")
