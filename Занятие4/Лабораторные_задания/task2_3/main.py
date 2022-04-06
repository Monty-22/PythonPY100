def task(num):
    list_digits = [int(digit) for digit in str(abs(num))]
    return True if 10 <= sum(list_digits) <= 99 else False
    # TODO добавить аннотацию типов
    ...  # TODO найти сумму цифр числа и понять двузначная ли она


if __name__ == "__main__":
    print(task(12))
    print(task(555))
    print(task(-12))
    print(task(-149))
