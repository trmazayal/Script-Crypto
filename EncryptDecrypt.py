# implement decrypt function caesar cipher

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
    
def encrypt_rail_fence(plaintext, key):
    rail = [['\n' for i in range(len(plaintext))]
                  for j in range(key)]
     
    # to find the direction
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(plaintext)):
         
        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        # fill the corresponding alphabet
        rail[row][col] = plaintext[i]
        col += 1
         
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(plaintext)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))

def decrypt_rail_fence(ciphertext, key):
    rail = [['\n' for i in range(len(cipher))]
                  for j in range(key)]
     
    # to find the direction
    dir_down = None
    row, col = 0, 0
     
    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        # place the marker
        rail[row][col] = '*'
        col += 1
         
        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
             
    # now we can construct the
    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
         
        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))



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

# cipher = 'EAASRFSLOSLMTOEAIKM'
# plain = decrypt_rail_fence(cipher, 2)
# print(plain)

plain = 'KIRIMDUIT'
cipher = encrypt_vigenere(plain, 'BATAVIA')
print("cipher: ", cipher)

c = 'LIKIHLUJT'
d = 'SDHTERIMA'

# find the key of vigenere cipher from two plaintext
def find_key(c, d):
    key = ''
    for i in range(len(c)):
        key += chr((ord(c[i]) - ord(d[i])) % 26 + ord('A'))
    return key

key = find_key(c, d)
print("key: ", key)

# decrypt the ciphertext using the key
plain = decrypt_vigenere(cipher, key)
print("plain: ", plain)