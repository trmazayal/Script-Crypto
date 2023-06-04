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
    rail = [['\n' for i in range(len(ciphertext))]
                  for j in range(key)]
     
    # to find the direction
    dir_down = None
    row, col = 0, 0
     
    # mark the places with '*'
    for i in range(len(ciphertext)):
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
        for j in range(len(ciphertext)):
            if ((rail[i][j] == '*') and
               (index < len(ciphertext))):
                rail[i][j] = ciphertext[index]
                index += 1
         
    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
         
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

def main():
    plaintext = "Hello World"
    key = 3
    print("Plain Text: " + plaintext)
    print("Key: " + str(key))
    ciphertext = encrypt_rail_fence(plaintext, key)
    print("Cipher Text: " + ciphertext)
    print("Decrypted Text: " + decrypt_rail_fence(ciphertext, key))
    
if __name__ == "__main__":
    main()