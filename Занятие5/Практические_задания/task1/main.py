if __name__ == "__main__":
    # матрица или таблица это список строк,
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row_index in matrix:
        for col_index in row_index:  # TODO как получить количество столбцов?
            print(col_index, end=" ")
        print()
