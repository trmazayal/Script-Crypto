from math import gcd
from prettytable import PrettyTable

def main():
    p = 19
    res = power_of_integer_by_modulo(p)
    print(res)
    
    primitive_roots = primRoots(p)
    print(primitive_roots)
    print()
    
    zz = {5:83}
    for z, p in zz.items():
        print(z, p, checkPrimRoots(z,p))


def checkPrimRoots(g,modulo):
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
    if required_set == actual_set:
        return True
    return False

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)           
    return roots

def power_of_integer_by_modulo(modulo):
    table = PrettyTable()
    header = ['g'] +['is_prim_root'] + [f'a{i}' for i in range(1,modulo)]
    table.field_names = header
    for g in range(1, modulo):
        row = [g, checkPrimRoots(g,modulo)]
        for a in range(1, modulo):
            row.append(pow(g, a) % modulo)
        table.add_row(row)
    return table

if __name__ == "__main__":
    main()