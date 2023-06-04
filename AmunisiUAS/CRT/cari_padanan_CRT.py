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


def verify_congruence(pair,m1,m2):
    M = m1 * m2
    M1 = M // m1
    M2 = M // m2
    M1_inv = find_modular_inverse(M1, m1)
    M2_inv = find_modular_inverse(M2, m2)
    
    print(f"{pair} ->", end=' ')
    print(f"a1M1M1_inv + a2M2M2_inv")
    print(f"        ({pair[0]})({m1})({M1_inv}) + ({pair[1]})({m2})({M2_inv}) mod {M}")
    
    x, y = pair
    
    res = (x * m1 * M1_inv + y * m2 * M2_inv) % (M)
    return res

m1 = 5
m2 = 7
pair = (4, 3)

sepadan = verify_congruence(pair, m1, m2)
print("Padanan dari", pair, "dengan unsur dari Z35 adalah", sepadan)
