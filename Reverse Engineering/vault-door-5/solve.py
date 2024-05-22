from base64 import b64decode


def url_decode(encoded: str) -> str:
    result = ""
    # Each character represants by a % sign and 2 hex digits
    for i in range(1, len(encoded), 3):
        result += chr(int(encoded[i : i + 2], 16))
    return result


def base64_decode(encoded: str) -> str:
    return b64decode(encoded.encode()).decode()


result = (
    "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
    + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
    + "JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1"
)

password = url_decode(base64_decode(result))
print(f"Flag is: picoCTF{{{password}}}")
