#Конушкина П.М.
#Вариант 11
'''Практическая 2 - Составить программу, печатающую значение True, если следующие указанные
высказывания являются истинными, и значение false — в противном случае. Целая и
дробная части заданного вещественного числа одинаковые.'''
def check_equal_parts(number):
  
    integer_part = int(number)

    fractional_part = round(number - integer_part, 10)
    

    fractional_str = str(fractional_part).split('.')[1]
    

    fractional_str = fractional_str.rstrip('0')

    return str(integer_part) == fractional_str


number = float(input("Введите вещественное число: "))
result = check_equal_parts(number)
print(result)
