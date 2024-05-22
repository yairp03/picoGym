from pathlib import Path


def parse_values_from_line(line: str) -> list[str]:
    return [v.strip() for v in line.split(",") if v.strip()]


with Path("./VaultDoor6.java").open() as java_file:
    values_lines = java_file.readlines()[29:33]

values = []
for line in values_lines:
    values.extend([int(v, 16) for v in parse_values_from_line(line)])

password = "".join([chr(v ^ 0x55) for v in values])

print(f"Flag is: picoCTF{{{password}}}")
