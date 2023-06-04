from collections import Counter

def main():
    n = 500


    res_prime_factorization = prime_factorization(n)
    print(f"phi({n}) = {calculation(n, res_prime_factorization)}")


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

def gcd(a, b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)
 
# A simple method to evaluate
# Euler Totient Function
def phi(n):
 
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result
 
def calculation(n, res_prime_factorization):
    # print how to calculate phi(n)
    print(f"phi({n}) = {n}", end="")
    for prime, power in res_prime_factorization:
        print(f" * (1 - 1/{prime})", end="")
    print()

    # calculate phi(n)
    result = n
    for prime, power in res_prime_factorization:
        result *= (1 - 1/prime)
    return int(result)


if __name__ == "__main__":
    main()