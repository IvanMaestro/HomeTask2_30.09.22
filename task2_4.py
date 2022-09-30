# * 4. Напишите программу, которая принимает на вход 2 числа. 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).

# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

first = int(input('Enter Position one: '))
second = int(input('Enter Position two: '))
elem_num = int(input('Enter Number of elements: '))
if first > elem_num * 2 + 1 or first < 1:
    print('Not such position, try again!')
    first = int(input('Enter Position one: '))
    second = int(input('Enter Position two: '))
    elem_num = int(input('Enter Number of elements: '))
elif second > elem_num * 2 + 1 or second < 1:
    print('Not such position, try again!')
    first = int(input('Enter Position one: '))
    second = int(input('Enter Position two: '))
    elem_num = int(input('Enter Number of elements: '))

new_list = list()
for k in range(-elem_num, 1):
    new_list.append(k)
for j in range(1, elem_num+1):
    new_list.append(j)

mult = new_list[first-1] * new_list[second - 1]

print(new_list, ' -> ', mult)