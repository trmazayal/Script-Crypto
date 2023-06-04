from tabulate import tabulate

# dlog(5, 10, 83)
def main():
    a = 5
    n = 83
    generate_modular(a,n)
    
    
def generate_modular(a, n):
    row = []
    for i in range(1, n):
        row.append(pow(a, i) % n)
    table = [row[i:i+10] for i in range(0, len(row), 10)]
    table.insert(0, ["-" * 10] * len(table[0]))
    table.insert(0,  [f"{j:2d}" for j in range(1, len(table[0])+1)])
    print(tabulate(table))
    return row

if __name__ == "__main__":
    main()
