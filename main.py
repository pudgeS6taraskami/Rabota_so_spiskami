#Работа со списками
#На 3
# Заполнение массива значениями с консоли
n = int(input("Введите размер массива: "))
array = []
for i in range(n):
    num = int(input("Введите число: "))
    array.append(num)

# Нахождение максимального значения циклом
max_value = array[0]
for i in range(1, n):
    if array[i] > max_value:
        max_value = array[i]
print("Максимальное значение (цикл):", max_value)

# Нахождение максимального значения функцией
max_value = max(array)
print("Максимальное значение (функция):", max_value)

# Нахождение минимального значения циклом
min_value = array[0]
for i in range(1, n):
    if array[i] < min_value:
        min_value = array[i]
print("Минимальное значение (цикл):", min_value)

# Нахождение минимального значения функцией
min_value = min(array)
print("Минимальное значение (функция):", min_value)

# Нахождение среднего значения массива
avg_value = sum(array) / n
print("Среднее значение:", avg_value)

# Линейный поиск
search_value = int(input("Введите число для поиска: "))
found_index = -1
for i in range(n):
    if array[i] == search_value:
        found_index = i
        break
print("Индекс элемента (цикл):", found_index)

# Линейный поиск функцией
found_index = array.index(search_value) if search_value in array else -1
print("Индекс элемента (функция):", found_index)

# Количество элементов циклом
count = 0
for i in range(n):
    count += 1
print("Количество элементов (цикл):", count)

# Количество элементов функцией
count = len(array)
print("Количество элементов (функция):", count)

# Сумма значений циклом
sum_value = 0
for i in range(n):
    sum_value += array[i]
print("Сумма значений (цикл):", sum_value)

# Сумма значений функцией
sum_value = sum(array)
print("Сумма значений (функция):", sum_value)

# Произведение значений циклом
product = 1
for i in range(n):
    product *= array[i]
print("Произведение значений (цикл):", product)

# Произведение значений функцией
from functools import reduce
product = reduce(lambda x, y: x * y, array)
print("Произведение значений (функция):", product)
#На 4
import copy

list1 = [[1, 2, 3, 4], [1, 2, 3, 5]]
list2 = copy.deepcopy(list1)
list2[0][3] = 100
print(f'list1: {list1}\t list2: {list2}')

