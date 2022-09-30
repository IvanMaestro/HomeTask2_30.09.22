# 3. Задайте список из n чисел, 
# заполненный по формуле (1 + 1/n) ** n и 
# выведите на экран их сумму.

#     Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
import math
n = int(input('Enter number: '))
new_list = list()
for k in range(1,n):
    new_list.append(int((1 + 1/n) ** n))
for j in range(n, n+1):
    new_list.append(round(((1 + 1/n) ** n)))
count = 0
summa = 0
while count < n:
    summa += new_list[count]
    count+=1

print(new_list, '->', summa)


