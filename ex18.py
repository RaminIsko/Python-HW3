import random

length = int(input("В-те длину массива: "))
array = []

for i in range(length) :
    array.append(random.randint(0,10))

print(f"Изначальный массив: {array}")

n = int(input("В-те число: "))

result = 0

nearestNum = array[0] 
minDistance = n - array[0]  

for i in range(0, length):
    distance = n - array[i]
    if distance < minDistance:
        nearestNum = array[i]
        minDistance = distance

print(f"Близжайшее число в массиве {array} к числу {n} -> {nearestNum}")



