def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def encrypt_vigenere(plaintext, key):
    key = generateKey(plaintext, key)
    ciphertext = []
    for i in range(len(plaintext)):
        x = (ord(plaintext[i]) +
             ord(key[i])) % 26
        x += ord('A')
        ciphertext.append(chr(x))
    return("" . join(ciphertext))

def decrypt_vigenere(ciphertext, key):
    key = generateKey(ciphertext, key)
    plaintext = []
    for i in range(len(ciphertext)):
        x = (ord(ciphertext[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        plaintext.append(chr(x))
    return("" . join(plaintext))

def find_key(ciphertext, plaintext):
    key = ''
    for i in range(len(ciphertext)):
        key += chr((ord(ciphertext[i]) - ord(plaintext[i])) % 26 + ord('A'))
    return key

def main():
    # plaintext = "KIRIMDUIT"
    # key = "BATAVIA"
    # new_plaintext = "SDHTERIMA"
    
    # ciphertext = encrypt_vigenere(plaintext,key)
    # plaintext = decrypt_vigenere(ciphertext,key)
    # new_key = find_key(ciphertext, new_plaintext)
    
    ciphertext = 'MIGEGVEIM'
    key = 'KEREN'
    
    plaintext = decrypt_vigenere(ciphertext,key)
    
    print(f"plaintext: {plaintext}")
    print(f"key: {key}")
    print(f"ciphertext: {ciphertext}")
    # print(f"new plaintext: {new_plaintext}")
    # print(f"new key: {new_key}")

if __name__ == '__main__':
    main()