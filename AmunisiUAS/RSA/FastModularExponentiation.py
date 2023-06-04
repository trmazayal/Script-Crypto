from prettytable import PrettyTable

"""
    Menghitung a^b mod n
"""
def main():
    a = 7
    b = 560
    n = 561
    fast_modular_exponentiation(a,b,n)
    
def fast_modular_exponentiation(a, b, n):
    """
    Menghitung a^b mod n
    """
    c = 0
    d = 1
    bin_b = bin(b)[2:]
    k = len(bin_b)

    tbl = PrettyTable(["i", "bi", "c", "d"])
    tbl.align = "r"
    tbl.padding_width = 1

    for i in range(k):
        c *= 2
        d = (d * d) % n
        if bin_b[i] == '1':
            c += 1
            d = (d * a) % n
        tbl.add_row([k-i-1, bin_b[i], c, d])

    print(tbl)
    print("-" * 20)
    print(f"Hasil: {a}^{b} mod {n} = {d}")


if __name__ == "__main__":
    main()