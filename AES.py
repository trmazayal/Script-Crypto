def mixColumns(a, b, c, d):
    printHex(gmul(a, 2) ^ gmul(b, 3) ^ gmul(c, 1) ^ gmul(d, 1))
    printHex(gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1))
    printHex(gmul(a, 1) ^ gmul(b, 1) ^ gmul(c, 2) ^ gmul(d, 3))
    printHex(gmul(a, 3) ^ gmul(b, 1) ^ gmul(c, 1) ^ gmul(d, 2))
    print()


def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a


def printHex(val):
    return print('{:02x}'.format(val), end=' ')


# mixColumns(0x7C, 0xF2, 0x2B, 0xAB)  # columns first (vertical from left)
# mixColumns(0x6B, 0x30, 0x76, 0x77)
# mixColumns(0x01, 0xFE, 0x7B, 0x6F)
# mixColumns(0xD7, 0x63, 0xC5, 0x67)

mixColumns(0xAB,0X34,0X56,0X78) 
mixColumns(0xCD,0x90,0xEF,0x56)
mixColumns(0xEF,0xAB,0x12,0x78)
mixColumns(0x12,0xCD,0x34,0x90)

print("Remember to rotate/transpose.")

#3f 41 bb 74 
# 93 8a 62 9f 
# 49 ec e8 63 
# cc 5f 1c f4 