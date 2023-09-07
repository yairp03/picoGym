import hashlib

def get_dynamic_part(username: bytes) -> str:
    sha = hashlib.sha256(username).hexdigest()
    return ''.join([sha[4], sha[5], sha[3], sha[6], sha[2], sha[7], sha[1], sha[8]])

print(f'picoCTF{{1n_7h3_|<3y_of_{get_dynamic_part(b"FREEMAN")}}}')
