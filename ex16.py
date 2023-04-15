import random

length = int(input("В-те длину массива: "))
array = []

for i in range(length) :
    array.append(random.randint(0,10))

print(f"Изначальный массив: {array}")

n = int(input("В-те число: "))

print(f"Количество числа {n} -> {array.count(n)}")