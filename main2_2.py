#Конушкина П.М.
#Вариант 11
'''Практическая 2 - Треугольник задан значениями углов и радиусом описанной окружности. Найти
длины сторон этого треугольника.'''
import math
a = int(input("Введите значение угла а: "))
b = int(input("Введите значение угла b: "))
c = int(input("Введите значение угла с: "))
R = int(input("Введите радиус описанной окружности R: "))

arad = math.radians (a)
brad = math.radians (b)
crad = math.radians (c)

aa = 2 * R * math. sin(arad)
bb = 2 * R * math. sin(brad)
cc = 2 * R * math. sin(crad)
print ("Длина стороны а: ",aa) 
print ("Длина стороны b: ",bb) 
print ("Длина стороны с: ",cc)