def print_operation_table(operation, num_rows=6, num_columns=6):
    table = []

    #данные сохраняем в массив в виде списка списков
    for j in range(1, num_columns + 1):
        column = []
        for i in range(1, num_rows + 1):
            value = operation(i, j)
            column.append(value)
        table.append(column)
    
    #заголовок
    print("    ", end="")
    for i in range(1, num_columns + 1):
        value_string = f"{i:>3}"
        print(f" {value_string}", end="")
    print()
    
    # разделители
    separator_string = "   +-" + "----" * num_columns
    print(separator_string)
    #данные
    for i in range(num_rows):
        row_string = f"{i+1:>2} |"
        for j in range(num_columns):
            value_string = f"{table[j][i]:>3}"
            row_string += f" {value_string}"
        print(row_string)
    print()

print_operation_table(lambda x,y: x**y, 4, 4)
print_operation_table(lambda x,y: x*y, 11, 11)