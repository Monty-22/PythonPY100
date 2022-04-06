def task(num: int):
    L = list(str(num))


    if str(4) in L and str(8) in L or str(9) in L:  # TODO записать условие
        print("Входят цифры (4 и 8) или цифра 9")
    else:
        print("Не входят цифры (4 и 8) или цифра 9")


if __name__ == "__main__":
    task(1234)
    task(12345678)
    task(1235679)
    task(0)
