# 5. ** Реализуйте алгоритм перемешивания списка. 
# Без функции shuffle из модуля random.

# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

# 1 Вариант. Используется random для выбора случайного индекса
#  Проблема - числа в новом списке повторяются
elem_num = int(input('Enter Number of elements: '))
import random
first_list = list()
for j in range(0, elem_num):
    first_list.append(j)

second_list = list()
for k in range(0, elem_num):
    i = random.randint(0,elem_num-1)
    second_list.append(first_list[i])

print(elem_num)
print('-> ', first_list)
print('-> ', second_list)

# 2 вариант. впринципе тоже неудачный.
# elem_num1 = int(input('Enter Number of elements: '))
# first_list1 = list()
# for j in range(0, elem_num1):
#     first_list1.append(j)

# second_list1 = list()
# i = 0
# for k in range(0, elem_num1):
#     if i == k:
#         i = elem_num1 - 3
#     elif i == elem_num1 - 1:
#         i *= 0
 
#     second_list1.append(first_list1[i])
#     i+=1


# print(elem_num1)
# print('-> ', first_list1)
# print('-> ', second_list1)