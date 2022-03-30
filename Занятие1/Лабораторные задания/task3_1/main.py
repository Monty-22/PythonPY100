list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти суммуб количество и среднее уникальных чисел
set_ = set(list_)
s = 0
count = 0
mean = 0
for n in set_:
    s = s + n
    count = count + 1

mean = s / count
print(s)
print(count)
print(mean)



