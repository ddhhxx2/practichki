#Конушкина П.М.
#Вариант 6
'''Практическая 3 - Известно, что одно из четырех чисел а1, а2, а3 и a4 отлично от трех других,
равных между собой. Присвоить номер этого числа переменной п.'''
import math
a1=2
a2=3
a3=2
a4=2 
if a1!=a2 and a3!=a2 and a4!=a2:
    n=a2
    print (n)
elif a2!=a3 and a4!=a3 and a1!=a3:
    n=a3
    print (n)
elif a2 != a4 and a1 != a4 and a3 != a4:
    n = a4
    print(n)
else:
    n=a1
    print(n)