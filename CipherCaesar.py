def decrypt_caesar(ciphertext,key):
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                plaintext += chr((ord(c) - 65 - key) % 26 + 65)
            else:
                plaintext += chr((ord(c) - 97 - key) % 26 + 97)
        else:
            plaintext += c
    return plaintext

def encrypt_caesar(plaintext,key):
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if c.isupper():
                ciphertext += chr((ord(c) - 65 + key) % 26 + 65)
            else:
                ciphertext += chr((ord(c) - 97 + key) % 26 + 97)
        else:
            ciphertext += c
    return ciphertext

def main():
    plaintext = "Hello World"
    key = 3
    ciphertext = encrypt_caesar(plaintext,key)
    print(ciphertext)
    plaintext = decrypt_caesar(ciphertext,key)
    print(plaintext)
    
if __name__ == '__main__':
    main()