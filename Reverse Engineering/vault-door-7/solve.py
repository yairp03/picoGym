from pathlib import Path


def unpack_number(number: int) -> str:
    return number.to_bytes(4).decode()


with Path("./VaultDoor7.java").open() as java_file:
    numbers_lines = java_file.readlines()[57:65]

numbers = []
before_number = "== "
for line in numbers_lines:
    number_index = line.index(before_number) + len(before_number)
    numbers.append(int(line[number_index:].strip(";\n")))

password = ""
for number in numbers:
    password += unpack_number(number)

print(f"Flag is: picoCTF{{{password}}}")
