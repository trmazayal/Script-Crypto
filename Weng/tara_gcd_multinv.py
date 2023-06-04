def gcd(a, b):
    print("q\tr\tx\ty\ta\tb\tx2\tx1\ty2\ty1")
    x2, x1, y2, y1 = 1, 0, 0, 1
    if b == 0:
        d, x, y = a, 1, 0
        return d, x, y
    else:
        q, r, x, y = '-', '-', '-', '-'
        print(q, r, x, y, a, b, x2, x1, y2, y1, sep = "\t")
        while b > 0:
            q = a // b
            r = a -q*b
            x = x2 - q*x1
            y = y2 - q*y1
            a = b
            b = r
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y
            print(q, r, x, y, a, b, x2, x1, y2, y1, sep = "\t")
        d = a
        x = x2
        y = y2
        return d, x, y
    
def multInv(a, b):
    print("q\tr\ty\ta\tb\ty2\ty1")
    q, r, y = '-', '-', '-'
    y2, y1 = 0, 1
    if b == 0:
        d, y = a, 0
        return d, y
    else:
        print(q, r, y, a, b, y2, y1, sep = "\t")
        while b > 0:
            q = a // b
            r = a - q*b
            y = y2 - q*y1
            a = b
            b = r
            y2 = y1
            y1 = y
            print(q, r, y, a, b, y2, y1, sep = "\t")
        d = a
        y = y2
        return d, y
