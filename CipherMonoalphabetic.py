def decrypt_monoalphabetic(ciphertext, key):
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                plaintext += key[ord(c) - 65]
            else:
                plaintext += key[ord(c) - 97].lower()
        else:
            plaintext += c
    return plaintext

def encrypt_monoalphabetic(plaintext, key):
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if c.isupper():
                ciphertext += chr(key.index(c) + 65)
            else:
                ciphertext += chr(key.index(c.upper()) + 97)
        else:
            ciphertext += c
    return ciphertext

def main():
    plaintext = "Hello World"
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    ciphertext = encrypt_monoalphabetic(plaintext,key)
    print(ciphertext)
    plaintext = decrypt_monoalphabetic(ciphertext,key)
    print(plaintext)