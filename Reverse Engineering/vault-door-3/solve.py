result_string = "jU5t_a_sna_3lpm12g94c_u_4_m7ra41"

password = [""] * 32  # Password length

for i in range(8):
    password[i] = result_string[i]

for i in range(8, 16):
    password[23 - i] = result_string[i]

for i in range(16, 32, 2):
    password[46 - i] = result_string[i]

for i in range(31, 16, -2):
    password[i] = result_string[i]

print(f"Flag is: picoCTF{{{''.join(password)}}}")
