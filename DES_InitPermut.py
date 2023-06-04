def init_permutation(hex):
    init_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                 60, 52, 44, 36, 28, 20, 12, 4,
                 62, 54, 46, 38, 30, 22, 14, 6,
                 64, 56, 48, 40, 32, 24, 16, 8,
                 57, 49, 41, 33, 25, 17, 9, 1,
                 59, 51, 43, 35, 27, 19, 11, 3,
                 61, 53, 45, 37, 29, 21, 13, 5,
                 63, 55, 47, 39, 31, 23, 15, 7]
    perm = ''
    for i in init_perm:
        perm += hex[i-1]
    return perm

def final_permutation(hex):
    final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
                  39, 7, 47, 15, 55, 23, 63, 31,
                  38, 6, 46, 14, 54, 22, 62, 30,
                  37, 5, 45, 13, 53, 21, 61, 29,
                  36, 4, 44, 12, 52, 20, 60, 28,
                  35, 3, 43, 11, 51, 19, 59, 27,
                  34, 2, 42, 10, 50, 18, 58, 26,
                  33, 1, 41, 9, 49, 17, 57, 25]
    perm = ''
    for i in final_perm:
        perm += hex[i-1]
    return perm

def hex2bin(hex):
    bin = ''
    for i in hex:
        bin += format(int(i, 16), '04b')
    return bin
    
def bin2hex(bin):
    hex = ''
    for i in range(0, len(bin), 4):
        hex += format(int(bin[i:i+4], 2), 'x')
    return hex


def DESAlgo(hex):
    bin = hex2bin(hex)
    perm = init_permutation(bin)
    hex = bin2hex(perm)
    return hex 

def main():
    hex = '0000000000000000'
    print(DESAlgo(hex))

if __name__ == '__main__':
    main()