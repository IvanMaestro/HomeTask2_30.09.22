# 1. Напишите программу, которая 
# принимает на вход вещественное 
# число и показывает сумму его цифр.

# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27
# 
# 1 Вариант

number = float(input('Введите число: '))
number = number * 10 ** 5
summa = 0
while number > 0:
    summa = summa + number % 10
    number = number // 10
print(int(summa))


# 2 Вариант

# str_num = input('Введите число: ')
# number = float(str_num.replace('.', ''))
# sum = 0
# while number > 0:
#     sum = sum + number % 10
#     number = number // 10
# print(int(sum))