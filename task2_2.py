# 2. Напишите программу, которая 
# принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

num = int(input('Введите число: '))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
   
i = num
my_list = [0] * i
while i > 0:
    fact = factorial(i)
    my_list[i-1] = fact
    i-=1

print(my_list)
