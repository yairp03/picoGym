from pathlib import Path


def parse_items_from_line(line: str) -> list[str]:
    return [v.strip() for v in line.strip().split(",") if v.strip()]


def parse_ascii_with_base(line: str, base: int) -> str:
    values = [chr(int(v, base=base)) for v in parse_items_from_line(line)]
    return "".join(values)


with Path("VaultDoor4.java").open() as java_file:
    lines = java_file.readlines()

decimals_str = parse_ascii_with_base(lines[32], 10)
hexes_str = parse_ascii_with_base(lines[33], 16)
octals_str = parse_ascii_with_base(lines[34], 8)
chars_str = "".join([v[1] for v in parse_items_from_line(lines[35])])

password = decimals_str + hexes_str + octals_str + chars_str

print(f"Flag is: picoCTF{{{password}}}")
