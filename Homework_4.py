# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# n = int(input("Введите количество чисел в первом наборе: "))
# m = int(input("Введите количество чисел во втором наборе: "))

first_set = set(input("Введите первый набор чисел через пробел: ").split())
second_set = set(input("Введите второй набор чисел через пробел: ").split())

union_sets = first_set.intersection(second_set)
result_list = list(union_sets)

for i in range(len(result_list)):
    result_list[i] = int(result_list[i])

for i in range(len(result_list)):
    for j in range(len(result_list) - 1):
        if result_list[j] > result_list[j + 1]:
            temp = result_list[j]
            result_list[j] = result_list[j + 1]
            result_list[j + 1] = temp

print(*result_list)