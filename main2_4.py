#Конушкина П.М.
#Вариант 11
'''Практическая 2 - Составить программу, которая печатает True, если точка с координатами (х, у)
принадлежит заданным закрашенным (заштрихованным) областям, показанным на
рисунках в табл. 1, и false — в противном случае.'''
import math
x=int(input ( "Введите координату точки по Х: "))
y=int(input ( "Введите координату Точки по Y: "))
r=int(input ("Введите радиус: "))
if x>6 or x<2 or y>6 or y<-6:
    print ("Точка за пределами круга")
gip2 = x**2 + y**2
gip1 = math.sqrt (gip2)
if gip1 > r:
    print ("False")
else:
    print ("True")