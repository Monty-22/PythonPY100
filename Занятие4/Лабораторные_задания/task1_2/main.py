def task(n, m):
    return [i**2 for i in range(n, m + 1) if i % 2 != 0]

    # TODO указать аннотацию типов
    ...  # TODO с помощью list comprehension отфильтровать знаечения


if __name__ == "__main__":
    number_n = 5
    number_m = 37
    print(task(5, 37))
