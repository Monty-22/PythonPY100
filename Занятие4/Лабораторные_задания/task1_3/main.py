def count_even_numbers(list_numbers: list) -> int:


    L = [i for i in list_numbers if i % 2 == 0]
    return len(L)
    ...  # TODO найти количество четных чисел в списке list_numbers


if __name__ == "__main__":
    print(count_even_numbers(list(range(1, 25))))
