tuple_ = (8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9)
sum = 0
count = 0
mean = 0
min = tuple_[0]
max = tuple_[0]
for x in tuple_:
    sum += x
    count += 1
    if min > x:
        min = x
    if max < x:
        max = x
mean = sum / count

print(sum)
print(count)
print(mean)
print(min)
print(max)


# TODO Каждое из значений печатать на отдельной строке
