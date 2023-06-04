def find_modular_inverse(a, m):
    # Algoritma Extended Euclidean
    if m == 1:
        return 0

    original_m = m
    x, y = 1, 0

    while a > 1:
        q = a // m
        a, m = m, a % m
        x, y = y, x - q * y

    if x < 0:
        x += original_m

    return x

def find_congruence(A,pair):
    m1, m2 = pair
    
    M = m1 * m2
    print(f"m1 = {m1}, m2 = {m2}")
    print(f"M = m1*m2 = {M}")
    print(f"A = {A}")
    
    M1 = M // m1
    M2 = M // m2
    
    M1_inv = find_modular_inverse(M1, m1)
    M2_inv = find_modular_inverse(M2, m2)
    
    print(f"M1 = M/m1 = {M1}, M2 = M/m2 = {M2}")
    print(f"M1_inv = {M1_inv}, M2_inv = {M2_inv}")
    
    crt_representation = (A % m1, A % m2)
    return crt_representation, (M1, M2), (M1_inv, M2_inv)

def calculate_congruence(pair, crt_representation, times):
    # To multiply 1651 by 72 (mod 1813)
    m1, m2 = pair
    x, y = crt_representation
    
    x_res = (x * times) % m1
    y_res = (y * times) % m2
    print(f'({x} * {times} mod {m1}), ({y} * {times} mod {m2})')
    return x_res, y_res

def verify_congruence(result, M , M_inv):
    print(f"{result} ->", end=' ')
    print(f"a1M1M1_inv + a2M2M2_inv")
    print(f"        ({result[0]})({M[0]})({M_inv[0]}) + ({result[1]})({M[1]})({M_inv[1]}) mod {M[0] * M[1]}")
    
    x, y = result
    M1, M2 = M
    M1_inv, M2_inv = M_inv
    
    res = (x * M1 * M1_inv + y * M2 * M2_inv) % (M1 * M2)
    return res

def main():
    A = 1651
    pair = (37, 49)
    crt_representation, M, M_inv = find_congruence(A,pair)
    print(f"crt_representation of {A} = {crt_representation}")
    print('-'*50)

    A_times_x = 72
    result = calculate_congruence(pair, crt_representation, A_times_x)
    print(f'To multiply {A} by {A_times_x} (mod {M[0] * M[1]}) = {result}')
    print('-'*50)
    
    # verify result
    res = verify_congruence(result, M, M_inv)
    print(f"        res = {res} (mod {M[0] * M[1]})")
    
if __name__ == "__main__":
    main()