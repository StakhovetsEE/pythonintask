#Задача 5 Вариант 17.
#Напишите программу, которая бы при запуске случайным образом отображала название одной из трех стран, входящих в военно-политический блок "Тройственный союз".

#Stakhovets E.E.
#23.05.2016
import random
print("Программа выводит на экран одну из трех стран, входящих в военно-политический блок 'Тройственный союз'")
a = random.choice(['Германия', 'Австро-Венгрия', 'Италия'])
print (a)
input("\nНажмите Enter")