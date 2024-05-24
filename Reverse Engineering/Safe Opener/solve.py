import base64


def base64_decode(encoded: str) -> str:
    return base64.b64decode(encoded.encode()).decode()


encoded_password = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"

print(f"Flag is: picoCTF{{{base64_decode(encoded_password)}}}")
