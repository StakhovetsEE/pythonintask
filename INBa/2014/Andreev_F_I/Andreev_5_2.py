# Задача 5, Вариант 2 
# Напишите программу, которая бы при запуске случайным образом отображала имя одного из трех поросят.

# Андреев Ф.И.
# 24.05.2016

import random
print('Программа случайным образом отображает имя одного из трех поросят')
feat = random.randint(1,3)
print('Поросята', end=" ")
if feat == 1 :
    print("Первый: Ниф-ниф")
elif feat == 2 :
    print("Второй: Наф-наф")
elif feat == 3:
    print("Третий: Нуф-нуф")
input ('Нажмите Enter для выхода')