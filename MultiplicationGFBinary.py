XOROP = '00011011'
lst = []

def shifting(num):
    # shift left binary of string
    if num[0] == '1':
        tmp = num[1:]
        tmp += '0'
        return xor_rop(tmp)
    tmp = num[1:]
    tmp += '0'
    return tmp

def xor_rop(num):
    # xor binary of string
    tmp = ''
    for i in range(len(num)):
        if num[i] == XOROP[i]:
            tmp += '0'
        else:
            tmp += '1'
    return tmp


def separate(num):
    bit1 = int(num,2) & 0b00000001
    bit2 = int(num,2) & 0b00000010
    bit3 = int(num,2) & 0b00000100
    bit4 = int(num,2) & 0b00001000
    bit5 = int(num,2) & 0b00010000
    bit6 = int(num,2) & 0b00100000
    bit7 = int(num,2) & 0b01000000
    bit8 = int(num,2) & 0b10000000

    bit1 = bin(bit1)[2:].zfill(8)   # format as 8-bit binary string with leading zeros
    bit2 = bin(bit2)[2:].zfill(8)
    bit3 = bin(bit3)[2:].zfill(8)
    bit4 = bin(bit4)[2:].zfill(8)
    bit5 = bin(bit5)[2:].zfill(8)
    bit6 = bin(bit6)[2:].zfill(8)
    bit7 = bin(bit7)[2:].zfill(8)
    bit8 = bin(bit8)[2:].zfill(8)
    
    return [bit1, bit2, bit3, bit4, bit5, bit6, bit7, bit8]
    
def main():
    
    A = '01010111'
    B = '10000011'
    
    for i in range(8):
        lst.append(A)
        A = shifting(A)
    separate_b = separate(B)
    print(lst)
    print(separate_b)
    
    binary_list = []
    for i in range(len(separate_b)):
        if separate_b[i] != '00000000':
            binary_list.append(lst[i])
            
    binary_list = [bin(int(s, 2))[2:].zfill(max(map(len, binary_list))) for s in binary_list]

    result = int(binary_list[0], 2)
    for binary_str in binary_list[1:]:
        result ^= int(binary_str, 2)

    res = bin(result)[2:].zfill(8)
    print(res)
        
if __name__ == '__main__':
    main()