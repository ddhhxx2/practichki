#Конушкина П.М.
#Вариант 17
'''Практическая 9 - Дана последовательность из N вещественных чисел. Вычислить сумму чисел,
порядковые номера которых являются простыми числами.'''
sequence = [1.5, 2.3, 3.7, 4.1, 5,6, 6.2, 7.8, 8.4, 9.0, 10.2]
total_sum = 0
for index in range (len(sequence)):
    order_number = index + 1
    if order_number < 2: 
        is_prime = False
    else:
        is_prime = True
        for i in range (2, order_number-1):
            if order_number %i ==0:
                is_prime = False
                break
    if is_prime:
        total_sum += sequence[index]
print (f"Сумма чисел с простыми порядковыми номерами: {total_sum}")