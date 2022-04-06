def task(list_1):
    L = [i**3 if i > 0 else  0 for i in list_1]
    return L
    # TODO записать решение в виде функции
    ...


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    new_list = task(list_)
    print(new_list)
