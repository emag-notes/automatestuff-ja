table_data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


def print_table(data):
    col_widths = [0] * len(data)
    for each_col_index in range(0, len(data)):
        longest_length = 0
        for each_element_index in range(0, len(data[each_col_index])):
            if len(data[each_col_index][each_element_index]) > longest_length:
                longest_length = len(data[each_col_index][each_element_index])
                col_widths[each_col_index] = longest_length

    for inner in range(0, len(data[0])):
        for outer in range(0, len(data)):
            print(data[outer][inner].rjust(col_widths[outer]), end=' ')
        print()


print_table(table_data)
