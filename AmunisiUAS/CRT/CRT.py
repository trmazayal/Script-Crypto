from functools import reduce

# Dengan CRT, representasikan setiap unsur dari Z15* = 
# {1, 2, 4, 7, 8, 11, 13, 14} sebagai unsur dari Z5* x Z3*.
# 14 -> (4, 2), 13 -> (3, 1)
def z_n_star(n):
    return n, [i for i in range(1, n) if gcd(i, n) == 1]

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def crt_mapping(z1, z2, z3):
    n1, z1_star = z1
    n2, z2_star = z2
    n3, z3_star = z3
    
    mapping = {}
    for num in z1_star:
        mod_n2 = num % n2
        mod_n3 = num % n3
        print(f'{num} -> ({mod_n2}, {mod_n3})')
        mapping[num] = (mod_n2, mod_n3)

    return mapping


def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 

def main():
    z1 = z_n_star(15)
    z2 = z_n_star(5)
    z3 = z_n_star(3)
    
    res = crt_mapping(z1, z2, z3)

    # Langkah 1: Operasi dengan modulo 5
    # 14 mod 5 = 4
    # 13 mod 5 = 3
    # 4 · 3 mod 5 = 12 mod 5 = 2

    # Langkah 2: Operasi dengan modulo 3
    # 14 mod 3 = 2
    # 13 mod 3 = 1
    # 2 · 1 mod 3 = 2 mod 3 = 2

    # Langkah 3: Menggabungkan hasil menggunakan CRT
    # Dalam CRT, kita perlu menyelesaikan sistem persamaan berikut:
    # x ≡ 2 (mod 5)
    # x ≡ 2 (mod 3)
    m = [5, 3]
    a = [2, 2]
    print(chinese_remainder(m, a))

    # Dengan menggunakan CRT, kita dapat menemukan solusi unik untuk x dengan modulo 15.
    # Karena kedua persamaan tersebut memiliki hasil yang sama (x ≡ 2), maka hasil dari 14 · 13 mod 15 adalah 2.

    # Jadi, 14 · 13 mod 15 = 2.            


if __name__ == "__main__":
    main()

    # Untuk menghitung ekspresi 11^53 mod 15 menggunakan CRT (Chinese Remainder Theorem), kita perlu menguraikan operasi tersebut menjadi dua operasi terpisah dengan modulo 5 dan modulo 3, kemudian menggabungkan hasilnya menggunakan CRT. Berikut adalah langkah-langkahnya:

    # Langkah 1: Operasi dengan modulo 5
    # 11^53 mod 5 = (11 mod 5)^53 mod 5 = 1^53 mod 5 = 1

    # Langkah 2: Operasi dengan modulo 3
    # 11^53 mod 3 = (11 mod 3)^53 mod 3 = 2^53 mod 3

    # Dalam hal ini, kita perlu menggunakan pola siklus sisa pangkat 2 dengan modulo 3:
    # 2^1 mod 3 = 2
    # 2^2 mod 3 = 1
    # 2^3 mod 3 = 2
    # 2^4 mod 3 = 1

    # Karena 53 adalah bilangan ganjil, maka pola siklus akan berulang dengan 2^53 mod 3 sama dengan 2^1 mod 3, yaitu 2.

    # Langkah 3: Menggabungkan hasil menggunakan CRT
    # Dalam CRT, kita perlu menyelesaikan sistem persamaan berikut:
    # x ≡ 1 (mod 5)
    # x ≡ 2 (mod 3)

    # Dengan menggunakan CRT, kita dapat menemukan solusi unik untuk x dengan modulo 15.
    # Karena kedua persamaan tersebut tidak memiliki hasil yang sama, kita tidak dapat langsung menentukan nilai x. Namun, kita dapat menggunakan kasus-kasus sederhana untuk mencari pola.

    # Menggunakan nilai x = 1, kita dapatkan:
    # 1 ≡ 1 (mod 5)
    # 1 ≡ 1 (mod 3)

    # Menggunakan nilai x = 6, kita dapatkan:
    # 6 ≡ 1 (mod 5)
    # 6 ≡ 0 (mod 3)

    # Menggunakan nilai x = 11, kita dapatkan:
    # 11 ≡ 1 (mod 5)
    # 11 ≡ 2 (mod 3)

    # Karena x = 11 memenuhi kedua persamaan, maka hasil dari 11^53 mod 15 adalah 11.

    # Jadi, 11^53 mod 15 = 11.