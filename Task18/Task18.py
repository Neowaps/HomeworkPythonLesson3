# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

n = int(input("Введите длину массива: "))
x = int(input("Введите элемент: "))
array = [randint(1, 10) for i in range(n)]
print(array)

difference = abs(x - array[0])
for i in range(len(array)):
    if abs(x - array[i]) <= difference:
        difference = abs(x - array[i])
        result = array[i]
print(f"Самый близкий по величине элемент к заданному числу: {result}")
