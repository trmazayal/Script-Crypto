class ExtEuclGcdRow:
    def __init__(self, q, r, x, y, a, b, x2, x1, y2, y1):
        self.q = q
        self.r = r
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.x2 = x2
        self.x1 = x1
        self.y2 = y2
        self.y1 = y1

    def as_list(self):
        return [self.q, self.r, self.x, self.y, self.a, self.b, self.x2, self.x1, self.y2, self.y1]

    def __repr__(self):
        return repr(self.as_list())


def extGcdGetList(a, b):
    rows = []
    rows.append(
            ExtEuclGcdRow('-', '-', '-', '-', a, b, 1, 0, 0, 1),
        )
    while True:
        q, r, x, y, a, b, x2, x1, y2, y1 = rows[-1].as_list()
        if b == 0:
            break
        q = a // b
        
        r = a - q*b  # or a % b
        a, b = b, r
        
        x = x2 - q*x1
        x2, x1 = x1, x

        y = y2 - q*y1
        y2, y1 = y1, y
        rows.append(
                ExtEuclGcdRow(q, r, x, y, a, b, x2, x1, y2, y1)
            )
    return rows


def printExtGcd(a, b):
    length = max(len(str(a)), len(str(b))) + 2

    headers = ['q', 'r', 'x', 'y', 'a', 'b', 'x2', 'x1', 'y2', 'y1']
    for header in headers:
        print(f"{header:>{length}s}", end="")
    print()
    
    rows = extGcdGetList(a, b)
    for row in rows:
        print()
        data = row.as_list()
        for datum in data:
            datum = str(datum)
            print(f"{datum:>{length}s}", end="")
    print()
    print()
    print(f"a*{row.x2} + b*{row.y2} == {row.a}")


def matrix_mult(matrix1: list[list], matrix2: list[list]):
    h = len(matrix1)
    w = 0 if h == 0 else len(matrix1[0])
    assert w == h

    res = [[0] * w for _ in range(h)]
    for row in range(h):
        for col in range(w):
            for x in range(w):
                operand_from_mtx1 = matrix1[row][x]
                operand_from_mtx2 = matrix2[x][col]
                res[row][col] += operand_from_mtx1 * operand_from_mtx2
    return res