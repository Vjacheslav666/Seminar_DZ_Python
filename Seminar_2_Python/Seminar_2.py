print("Домашняя работа 2 семинара!")
print("Домашняя работа включает 5 заданий.")
numbers = int(input("Введите цифру от 1 до 4: "))

if(numbers == 1):
    print("Это первая задача домашней работы!")
    print("Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.")
    
    n = int(input("Введите число N: "))
    mas = []
    count = 1
    for i in range(1, n + 1):
        count = count * i
        mas.append(count)
    print(f"N = {n}. Результат {mas}")
    

elif(numbers == 2):
    print("Это вторая задача домашней работы!")
    print("Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.")
    
    n = int(input("Введите целое число N: "))
    i = 2
    while n % i != 0:
        i += 1
    print(f"Наименьший натуральный делитель целого числа {n} равен: {i}")
    
    

elif(numbers == 3):
    print("Это третья задача домашней работы!")
    print("Задайте список из N элементов, заполненных числами из промежутка [-N, N].")
    print("Найдите произведение элементов на указанных позициях.")
    print("Пять позиций хранятся в списке, который вы сами заполняете.") # Эту часть не понял!
    
    n = int(input("Задайте список из N элементов: "))
    m = n * -1
    mas = []
    for i in range(m, n + 1):
        mas.append(i)
    print(mas)
    a = int(input(f"Укажите первый элемент на позициях от 0 до {n * 2}: "))
    b = int(input(f"Укажите второй элемент на позициях от 0 до {n * 2}: "))
    resultat = mas[a] * mas[b]
    print(f"Результат произведения двух выбранных элементов списка равен: {resultat}")
    

elif(numbers == 4):
    print("Это четвертая задача домашней работы!")
    print("Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.")
    n = int(input("Введите число N: "))
    mas = []
    count = 0
    for i in range(1, n + 1):
        mas.append(i)
        if i % 2 == 0:
            count = count + i
    print(f"Список состоит из: {mas}")
    print(f"Сумма чётных чисел от 1 до {n} равна: {count}")
    
    

else:
    print("Вы ввели неправильное число!")