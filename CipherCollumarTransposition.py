def encrypt_columnar_transposition(plaintext, key):
    ciphertext = ""
    for i in range(len(key)):
        for j in range(len(plaintext)):
            if j % len(key) == key.index(i + 1):
                ciphertext += plaintext[j]
    return ciphertext

def decrypt_columnar_transposition(ciphertext, key):
    plaintext = ""
    for i in range(len(key)):
        for j in range(len(ciphertext)):
            if j % len(key) == key.index(i + 1):
                plaintext += ciphertext[j]
    return plaintext

def main():
    plaintext = "KIRIMDUIT"
    key = [2, 5, 4, 3, 1]
    ciphertext = encrypt_columnar_transposition(plaintext, key)
    plaintext = decrypt_columnar_transposition(ciphertext, key)
    print(f"plaintext: {plaintext}")
    print(f"key: {key}")
    print(f"ciphertext: {ciphertext}")
    
if __name__ == '__main__':
    main()