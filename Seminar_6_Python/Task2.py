# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12, 'sadf', 5643] ---> ['sadf'] ,[12, 5643]

# Способ 1:
# spis = [12, 'sadf', 5643]
# word =[]
# number = []
# for i in spis:
#     if type(i) == str:
#         word.append(i)
#     elif type(i) == int:
#         number.append(i)
# print(word, number, sep="\n")

# Способ 2:
spis = [12, 'sadf', 5643]
f1 = filter(lambda x: type(x) is str, spis)
f2 = filter(lambda x: type(x) is int, spis)

print(list(f1), list(f2), sep=", ")



