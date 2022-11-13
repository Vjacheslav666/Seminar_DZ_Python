# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0, 56 -> 11

# Способ 1
# num = input('Введите вещественное число: ')
# sum = 0
# for i in num:
#     if i != '.':
#         sum += int(i)
# print(sum)

# Способ 2
def sum_digits(num):
    return sum(map(int, num.replace('.','').replace('-','')))

num = input('Введите любое вещественное число: ')
print(f'Сумма цифр в этом числе равна {sum_digits(num)}')