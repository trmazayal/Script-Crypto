# calculate xor of matrix 4x4

def xor(a, b):
    return a ^ b

def xor_matrix(matrix1, matrix2):
    matrix3 = []
    for i in range(len(matrix1)):
        matrix3.append([])
        for j in range(len(matrix1[i])):
            matrix3[i].append(xor(int(matrix1[i][j], 16), int(matrix2[i][j], 16)))
    # convert into hex
    for i in range(len(matrix3)):
        for j in range(len(matrix3[i])):
            matrix3[i][j] = hex(matrix3[i][j])
    return matrix3


def multiply_matrix(matrix1, matrix2):
    res = [[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                # resulted matrix
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return convert_to_hex(res)
            
def convert_to_hex(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = hex(matrix[i][j])
    return matrix

def convert_to_dec(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j], 16)
    return matrix

matrix1 = [['02','03', '01', '01'],
           ['01', '02', '03', '01'],
           ['01', '01', '02', '03'],
              ['03', '01', '01', '02']]

matrix2 = [['7C', '6B', '01', 'D7'],
              ['F2', '30', 'FE', '63'],
                ['2B', '76', '7B', 'C5'],
                    ['AB', '77', '6F', '67']]

matrix1dec = convert_to_dec(matrix1)
matrix2dec = convert_to_dec(matrix2)
print(matrix1dec)
print(matrix2dec)
print(multiply_matrix(matrix1dec, matrix2dec))
