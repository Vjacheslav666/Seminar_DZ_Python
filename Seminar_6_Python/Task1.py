# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.

# [1,2,3,4,22,234,24] ----> [22, 24]

# Способ 1:
lst = list(map(int, input("Введите цифры через пробел: ").split()))
f = filter(lambda x: 10 <= x < 100, lst)
spis = []
for l in f:
    spis.append(l)

print(spis)

# способ 2:
# coll = int(input("Введите общее колличество цифр: "))
# count = 1
# spis = []
# spis2 = []
# for i in range(coll):
#     sp = int(input(f"Введите {count} число: "))
#     spis.append(sp)
#     count += 1

# filtr = filter(lambda x: 10 <= x < 100, spis)
# for j in filtr:
#     spis2.append(j)
# print(spis2)