#Конушкина П.М.
#Вариант 11
'''Практическая 2 - Вычислить значения по следующим формулам при действительных значениях всех
переменных:'''
import math
a=int(input ("Введите значение а: "))
b=int(input ("Введите значение b: "))
c=int(input ("Введите значение с: "))
otv = ((b + (math.sqrt(b**2+(4*a*c)))) / (2*a)) - (a**3*c + (b**-2))
print ("Ответ: ", otv)



x=int(input ("Введите значение x: "))
y=int(input ("Введите значение у: "))
otv2 = (math.cos(x))/((math.pi - 2*x)) + (16*x*math.cos(x*y))
print ("Ответ: ", otv2 )