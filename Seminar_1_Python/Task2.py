# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Примечание:
# Используйте знания об Алгебра Логике, вы должны перебрать все возможные комбинации значений X, Y, Z (принимают значения 0 или 1).

print("Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.")
print("Примечание:")
print("Используйте знания об Алгебра Логике, вы должны перебрать все возможные комбинации значений X, Y, Z (принимают значения 0 или 1).")
for x in range(2):
    for y in range(2):
        for z in range(2):
            # ¬ -- not
	        # ⋁ -- or
	        # ⋀ -- and
            print(not (x or y or z) == (not x and not y and not z))
            print(x, y, z)