number = 123

d_1 = number // 100
d_2 = number % 100 // 10 # TODO найти число десятков
d_3 = number % 10 # TODO найти число единиц

list_digit =  [d_1,d_2,d_3]
print(list_digit)

print("Сумма цифр", sum(list_digit))
print("Количество цифр", d_1)  # TODO количество цифр
print("Минимальная цифра", d_2)
print("Максимальная цифра", d_3)  # TODO максимальная цифра
