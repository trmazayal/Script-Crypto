from collections import Counter

def prime_factorization_flat(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append((int(n)))
            break
    return factors


def prime_factorization(n):
    """
    Mengembalikan dalam format [(prime, power), ...]
    """
    ret = prime_factorization_flat(n)
    return sorted(Counter(ret).items())

print(prime_factorization(500))