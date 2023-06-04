
def print_table_with_headers(headers, column_headers, table, header_separator=True):
    assert len(table) == len(column_headers)

    new_table = table
    new_table_additional_width = 0
    
    if header_separator:
        new_table_additional_width += 1
        column_header_separator = [''] * len(column_headers)
        new_table = append_horizontally(transpose([column_header_separator]), new_table)
        
    new_table = append_horizontally(transpose([column_headers]), new_table)
    new_table_additional_width += 1

    if header_separator:
        row_header_separator = [''] * (len(headers) + new_table_additional_width)
        new_table = append_vertically([row_header_separator], new_table)

    new_row_header = ['']*new_table_additional_width + headers
    new_table = append_vertically([new_row_header], new_table)


    max_length = [
        get_list_str_max_len(headers),
        get_list_str_max_len(column_headers),
        get_table_str_max_len(table),
    ]
    max_length = max(max_length)
    print_table(new_table, max_length)
    

def print_table(table, max_length: int):
    margin = 2
    str_width = max_length + margin
    
    for curr_row in table:
        print_array_of_str_with_fixed_length(curr_row, str_width)


def print_array_of_str_with_fixed_length(arr, length):
    for string in arr:
        print(str(string).rjust(length), end="")
    print()


def get_list_str_max_len(lst):
    maks = 0
    for i in lst:
        maks = max(maks, len(str(i)))
    return maks

def get_table_str_max_len(list_of_list):
    maks = 0
    for lst in list_of_list:
        lst_maks = get_list_str_max_len(lst)
        maks = max(maks, lst_maks)
    return maks

def transpose(table):
    return list(map(list, zip(*table)))

def append_horizontally(table1, table2):
    assert len(table1) == len(table2), (len(table1), len(table2))
    table = []
    for row1, row2 in zip(table1, table2):
        table.append(row1 + row2)
    return table

def append_vertically(table1, table2):
    assert table1 == table2 == [] or len(table1[0]) == len(table2[0]), (len(table1[0]), len(table2[0]))
    return [row[:] for row in table1] + [row[:] for row in table2]

