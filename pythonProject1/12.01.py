# #29
# a = 13.12
# b= 0.62
# c = - 11.37
# d = 0.3965
# z = 0.16
#
#
#
# vozduh = input("Введите темпрературу воздуха :")
# veter = input("Введите скорость ветра : ")
#
#
# WCI = a + b * vozduh + c * veter ** z + d *vozduh * veter ** z


##################


# chisla = int(input("Введите первое целое число :"))
# chisla_2 = int(input("Введите второе целое число :"))
# chisla_3 = int(input("Введите третье целое число :"))
#
# a = [chisla,chisla_3,chisla_2]
# a.remove(max(chisla,chisla_3,chisla_2))
# a.remove(min(chisla,chisla_3,chisla_2))
#
#
#
# print("Ваше минимальное веденное число было : ",min(chisla,chisla_3,chisla_2))
# print("Ваше максимальное веденное число было : ",max(chisla,chisla_3,chisla_2))
# print('Ваше средне число : ', "".join(str(a)))



####

# chisla = int(input("Введите первое целое число :"))
# chisla_2 = int(input("Введите второе целое число :"))
# chisla_3 = int(input("Введите третье целое число :"))
#
# a = [chisla,chisla_3,chisla_2]
# a.sort()
#
#
#
#
# print("Ваше минимальное веденное число было : ", a[0])
# print("Ваше максимальное веденное число было : ", a[2])
# print("Ваше среднее число ", a[1])



################

# bread = 3.49
# skidka = 0.6
#
#
# bread_yesteday = int(input(" Введите количество купленых вчерашних булок : "))
# buhanka = bread * bread_yesteday
# skidka_2 = buhanka * skidka
#
# print("Обычная цена за буханку  :", bread)
# print("Обычная цена за буханку со скидкой :", bread * skidka)
# print("Ваше общая цена ровняется  :",skidka_2)
# #



###########
# bread = 3.49
# skidka = 0.6
# b = bread * skidka
#
#
# bread_today = int(input(" Введите количество купленых  булок : "))
# bread_yesteday = int(input(" Введите количество купленых вчерашних булок : "))
#
# today = bread_today * bread
# yest = bread * skidka * bread_yesteday
# b = today + yest
#
#
#
# print("Обычная цена за буханку  :", bread)
# print("Обычная цена за буханку со скидкой(вчерашнюю)  %1.1f" % b)
# print("Ваше цена за булки  : %1.1f" %today )
# print("Ваше цена за вчерашние булки  :%1.1f" % yest )
# print("Ваша общая цена  :%1.1f"% b )



#############
# zeloe  = int(input("Введите целое число : "))
#
#
# if zeloe % 2:
#     print("Ваше число не четное")
# else:
#     print("Ваше число четное ")

#########
# letter = input("Введите букву латинтского алфовита :")
#
# if letter == 'a' or letter == "e" or letter == 'i' or letter == "o" or letter == "u":
#     print("Эта буква гласная !")
# elif letter == "y":
#     print("Эта буква может быть как главсной , так и согласной")
# else:
#     print("Эта буква согласная ")

# from string import ascii_letters
#
#
#
#
#
# all_letters = ascii_letters
#
# letter = input("Введите букву латинтского алфовита :")
# letter = letter.lower()
#
#
# if len(letter.strip(all_letters)) != 0:
#     raise TypeError("Должны быть ток латинтские буквы ")
#
# else:
#
#     if letter == 'a' or letter == "e" or letter == 'i' or letter == "o" or letter == "u":
#         print("Эта буква гласная !")
#     elif letter == "y":
#         print("Эта буква может быть как гласной , так и согласной")
#     else:
#         print("Эта буква согласная ")
#


# ######
# fig = 0
#
# figure = int(input("Введите количесво фигур :"))
#
#
# if figure == 3:
#     fig = "Треугольник"
#
# elif figure == 4:
#     fig = "Квадрат"
#
# elif figure == 5:
#     fig = "Пятиугольник"
#
# elif figure == 6:
#     fig = "Шестиугольник"
#
# elif figure == 7:
#     fig = "Семиугольник"
#
# elif figure == 8:
#     fig = "Восьмиугольник"
#
# elif figure == 9:
#     fig = "Девятиугольник"
#
# elif figure == 10:
#     fig = "Десятиугольник"
#
# else:
#     fig = "Необходимо водить ток от 3 до 10 сторон"
#
# print("Ваша фигура это ", fig)



#######
# figure = int(input("Введите первую сторону треугольника :"))
# figure_2 = int(input("Введите вторую сторону треугольника :"))
# figure_3 = int(input("Введите третью сторону треугольника :"))
#
#
# if figure == figure_2:
#     if figure == figure_3:
#         print("Ваш треугольник является равностороний:")
#     else:
#         print("Ваш треугольник равнобедренный ")
#
# else:
#     print("Ваш треугольник разностороний")



##########
# day = None
#
#
# mouth = (input("Введите названия месяца :"))
# mouth = mouth.lower()
#
#
# if mouth == "январь" or mouth == "март" or mouth == "май" or mouth == "июль" or mouth == "август" or mouth == "октябрь" or mouth == "декабрь":
#     day = 31
#
# elif mouth == "апрель" or mouth == "июнь" or mouth == "сентябрь" or mouth == "ноябрь":
#     day = 30
#
# elif mouth == "февраль":
#     day = "Этот месяц может содержать и 28 и 29 дней"
#
# else :
#     raise TypeError("Ощибка при воде ")
#
#
#
# print("В Вашем месяце ", day ," дней")


# Gz = None
#
# note = input("Введите вашу ноту :")
# note = note.upper()
#
# if note == "C4":
#     Gz = 261.63
# elif note == "D4":
#     Gz = 293,66
# elif note == "E4":
#     Gz = 329,63
# elif note == "F4":
#     Gz = 349,23
# elif note == "G4":
#     Gz = 392,00
# elif note == "A4":
#     Gz = 440,00
# elif note == "B4":
#     Gz = 493,88
# else:
#     raise TypeError("Неверный вод")
#
# print(Gz)


# C4 = 261.63
# D4 = 293,66
# E4 = 329,63
#
# F4 = 349,23
# G4 = 440,00
# B4 = 493,88
# A4 = 493,88
#
# name = input("Введите вашу ноту :")
#
#
# note = name[0]
# oktava = int(name[1])
#
# if note == "C":
#     Gz = C4
# elif note == "D":
#     Gz = D4
# elif note == "E":
#     Gz = E4
# elif note == "F":
#     Gz = F4
# elif note == "G":
#     Gz = G4
# elif note == "A":
#     Gz = A4
# elif note == "B":
#     Gz = B4
#
#
#
# Gz = Gz / 2 ** (4 - oktava)
#
#
# print("Частота ноты ", name , "равна ", Gz)


shit = None

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 440.00
B4 = 493.88
A4 = 493.88

Gz = float(input("Ведите частоту звука :"))
Gz = [str(i) for i in Gz]

if Gz == C4 :
    shit = "C4"
elif Gz == D4:
    shit = "D4"
elif Gz == E4:
    shit = "E4"
elif Gz == F4:
    shit = "F4"
elif Gz == G4:
    shit = "G4"
elif Gz == B4:
    shit = "B4"
elif Gz == A4:
    shit = "A4"
else:
    print("Не правильный вод , либо введеной ноты не существует")


print("Ваша частота называется ", shit)







