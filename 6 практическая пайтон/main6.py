#Конушкина П.М.
# Вариант 1
'''Практическая 6 - Дано натуральное число k. Напечатать k-ю цифру последовательности 12345678910111213..., содержащую подряд все натуральные числа.'''
k = int (input ("Введите натуральное число k: "))
i = k
lenght = 1
count = 9 
start = 1
while i > lenght * count:
    i -=lenght*count
    lenght += 1
    count *= 10
    start *= 10
num = start + (i-1) // lenght 
digit_index = (i-1) % lenght
kth_digit = int(str(num)[digit_index])
print (f"{k}-я цифра в последовательности: {kth_digit}")