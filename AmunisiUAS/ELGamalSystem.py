def main():
    # Parameter umum (berlaku untuk semua user)
    # sebuah bilangan prima random p dan sebuah akar primitif a dari p.
    p = 19
    a = 2
    # Pembuatan kunci
    # Untuk membuat kuncinya, user A melakukan langkah-langkah:
    # 1. pilih kunci privat x berupa sebuah bilangan random yang lebih kecil dari p;
    # 2. hitung kunci publik y := a^x (mod p).
    x = 17
    # Enkripsi
    # Untuk mengirim plaintext rahasia m < p kepada user A, pengirim B memilih sebuah bilangan 
    # random k < p dan membuat ciphertext berupa pasangan (c1,c2) sebagai berikut:
    k = 13
    m = 15

    y = gen_key(a, x)
    print("Public Key: y := a^x (mod p)", y)
    print("Enkripsi: c1 := a^k (mod p) dan c2 := (y^k * m) (mod p)")
    c1, c2 = encryption(m, a, y, k, p)
    print("c1:", c1)
    print("c2:", c2)
    print("Dekripsi: m := (c1^x)^-1 * c2 (mod p)")
    m = decryption(c1, c2, x)
    print("m:", m)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse tidak ada')
    else:
        return x % m
    
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


def gen_key(q,x):
    public_key_y = pow(a, x) % p
    return public_key_y


def encryption(m,a,y,k,p):


    c1 = pow(a, k) % p
    c2 = (pow(y, k) * m) % p
    return c1, c2


def decryption(c1, c2,x):
    m = (modinv(pow(c1, x), p) * c2) % p
    return m


if __name__ == "__main__":
    main()