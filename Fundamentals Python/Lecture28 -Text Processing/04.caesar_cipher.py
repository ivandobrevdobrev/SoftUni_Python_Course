text = input()
encrypted_version = ""

for ch in text:
    encrypted_ch = chr(ord(ch) + 3)
    encrypted_version += encrypted_ch

print(encrypted_version)