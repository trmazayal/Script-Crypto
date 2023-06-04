from prettytable import PrettyTable

def main():
    x = 5
    a = 2
    b = -1
    
    
    # Table Y
    tableY = {}
    table = PrettyTable()
    header = ['x'] + [f'y^2 mod {x}']
    table.field_names = header
    print('Table Y')
    for i in range(0,x):
        y_2modx = (i**2) % x
        tableY[i] = y_2modx
        table.add_row([i,y_2modx])
    print(table)
    
    # Table X
    tableX = PrettyTable()
    header = ['x'] + [f'x^3 + {a}x + {b} ≡ y^2 mod {x}'] + ['y'] + ['points']
    tableX.field_names = header
    print('Table X')
    
    tableX_row2 = {}
    tableX_row2_detail = {}
    for i in range(0,x):
        x_3ab = ((i**3) + (a*i) + b)
        x_3ab_mod = x_3ab % x
        tableX_row2[i] = x_3ab_mod
        tableX_row2_detail[i] = f'{x_3ab_mod} ≡ {x_3ab} (mod {x})'
    
    tableX_row3 = {}
    for i in tableX_row2:
        row_i = []
        for key, value in tableY.items():
            if tableX_row2[i] == value:
                row_i.append(key)
        if len(row_i) > 0:
            tableX_row3[i] = row_i
        else:
            tableX_row3[i] = 'no solutions'
    
    tableX_row4 = {}
    for i in tableX_row3:
        row_i = []
        if tableX_row3[i] != 'no solutions':
            for j in tableX_row3[i]:
                row_i.append((i,j))
        else:
            row_i.append('-')
        tableX_row4[i] = row_i
    
    for i in range(0,x):
        tableX.add_row([i,tableX_row2_detail[i],tableX_row3[i],tableX_row4[i]])
    print(tableX)
    
    result = [0]
    print(f'E_{x}({a},{b}) = ', end='')
    for i in tableX_row4:
        if len(tableX_row4[i]) > 0:
            for j in range(0,len(tableX_row4[i])):
                if tableX_row4[i][j] != '-':
                    result.append(tableX_row4[i][j])
            
    print(result)
if __name__ == '__main__':
    main()