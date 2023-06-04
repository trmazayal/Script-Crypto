def build_key_playfair(key):
    #  build of key matrix with char I/J
    for i in range(0, len(key)):
        if key[i] == "J":
            key = key[:i] + "I" + key[i + 1 :]  
    key = key.replace("J", "")
    key = key.replace(" ", "")
    key = key.upper()
    key = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = "".join(dict.fromkeys(key))
    return key

def decrypt_playfair(ciphertext, key):
    key = build_key_playfair(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        x1, y1 = key.index(ciphertext[i]) // 5, key.index(ciphertext[i]) % 5
        x2, y2 = key.index(ciphertext[i + 1]) // 5, key.index(ciphertext[i + 1]) % 5
        if x1 == x2:
            plaintext += key[x1 * 5 + (y1 - 1) % 5]
            plaintext += key[x2 * 5 + (y2 - 1) % 5]
        elif y1 == y2:
            plaintext += key[((x1 - 1) % 5) * 5 + y1]
            plaintext += key[((x2 - 1) % 5) * 5 + y2]
        else:
            plaintext += key[x1 * 5 + y2]
            plaintext += key[x2 * 5 + y1]
    return plaintext

def encrypt_playfair(plaintext, key):
    key = build_key_playfair(key)
    if len(plaintext) % 2 == 1:
        plaintext += "X"
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        x1, y1 = key.index(plaintext[i]) // 5, key.index(plaintext[i]) % 5
        x2, y2 = key.index(plaintext[i + 1]) // 5, key.index(plaintext[i + 1]) % 5
        if x1 == x2:
            ciphertext += key[x1 * 5 + (y1 + 1) % 5]
            ciphertext += key[x2 * 5 + (y2 + 1) % 5]
        elif y1 == y2:
            ciphertext += key[((x1 + 1) % 5) * 5 + y1]
            ciphertext += key[((x2 + 1) % 5) * 5 + y2]
        else:
            ciphertext += key[x1 * 5 + y2]
            ciphertext += key[x2 * 5 + y1]
    return ciphertext

def main():
    plaintext = "Hello World"
    key = "Playfair Example"
    ciphertext = encrypt_playfair(plaintext, key)
    print(ciphertext)
    plaintext = decrypt_playfair(ciphertext, key)
    print(plaintext)

if __name__ == "__main__":
    main()