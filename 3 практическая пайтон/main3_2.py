#Конушкина П.М.
#Вариант 6
'''Практическая 3 - По трем заданным числам определить, является ли сумма каких-либо двух из
этих чисел положительной'''
import math
a=int(input ("Введите значение а: "))
b=int(input ("Введите значение b: "))
c=int(input ("Введите значение c: "))
if (a+b) > 0 or (a+c) > 0 or (b+c)>0:
    print ("схима каких-либо двух чисел положительная")
else:
    print ("сумма всех пар чисел отрицательная")