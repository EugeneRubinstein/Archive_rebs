
# dlina = float(input("Введите длину комнаты в метрах : "))
# shirina = float(input("Введите ширину комнаты в метрах : "))
#
# ploshad = dlina * shirina
#
#
# print("Ваша прощадь состовляет ",ploshad,'Квадратных метров')
#
#
#
# ###################################
# akr = 43560
#
# dlina = float(input("Введите длину садового участка : "))
# shirina = float(input("Введите ширину садового участка : "))
#
# ploshad = (dlina * shirina) / akr
#
# print('Общее количество акров',ploshad)
#
#
#
#
# #########
# lil = 0.10
# big =0.25
#
#
# lil_boutle = float(input("Ведите ваше количество бутылок меньше литра :"))
# boutle = float(input("Ведите ваше количество бутылок литровых или больше :"))
#
#
# refund = lil_boutle * lil + boutle *big
#
#
# print("Ваша выручка составит {}".     format(refund))
#
#
# ##########################
#
# chaivie = 0.18
# tax = 0.07
#
# summa = float(input('Введите сумму заказа в ресторане :'))
#
# chai_from_summa = summa * chaivie
# tax_from_summa = summa *tax
#
# all = summa + chai_from_summa + tax_from_summa
#
# print("Ваш налог состовляет :{}".format(tax_from_summa))
# print("Желательные чаевые от суммы : {}".format(chai_from_summa))
# print('Все вместе :',all)
#
#
#
# ####################
#
# import math
#
# a = int(input('Ведите число А:'))
# b = int(input('Ведите число B:'))
#
#
#
#
#
#
# print('Сумма А и B равна :',a+b)
# print('Произведение  А и B равно :',a*b)
# print('Частное от деление А и B равна :',a//b)
# print('Остаток от деление  А и B равна :',a%b)
# print('Десятичный алгоритм А равен :',math.log10(a))
# print('Результат возведения числа А в степени B равен :',a**b)
#
#
# ############
#
# one = 1
# two = 2
# five = 5
# ten = 10
# dva_5=25
# five_0=50
# one_d=100
# two_d=200
#
#
#
# cent = int(input('Введите суму сдачи в центах :'))
#
# print('Сдача : количество Двух доларовых монет :',cent // two_d)
# cent = cent % two_d
# print('Сдача : количество Однодоларовых монет :',cent//one_d)
# cent = cent%one_d
# print('Сдача : количество 50ти центовых монет :',cent//five_0)
# cent = cent%five_0
# print('Сдача : количество 25ти центовых монет :',cent//dva_5)
# cent = cent%dva_5
# print('Сдача : количество 10 центовых монет :',cent//ten)
# cent = cent%ten
# print('Сдача : количество 5 центовых монет :',cent//five)
# cent = cent%five
# print('Сдача : количество 2 центовых монет :',cent//two)
# cent = cent%two
# print('Сдача : количество 1 центовых монет :',cent//one)
#
#
#
# ##############
# djim_1 = 2.54
# fut_1 = 30.48
#
# fut = float(input('Введите количество футов :'))
# djim = float(input('Введите количество дюймов :'))
#
# sm = djim_1 * djim + fut_1 * fut
#
#
# print('Ваш рост в см :',sm)
#
#
# #############
# import math
#
# n = int(input("Ведите количество сторон :"))
# s = int(input("Ведите длину сторон :"))
#
#
# area = (n * s ** 2) / (4*math.tan(math.pi/n))
#
#
# print('Площадь :',area)
#
#
# #########
#
# sec = int(input("Введите количесво секунд :"))
# day = 86000
# hour = 3600
# min = 60
#
#
# D = sec // day % day
# H = sec // hour % hour
# M = sec // min % min
# S = sec % min
#
#
#
#
#
# print(D,":" ,H ,':', M ,":", S)
# print("{da} : {ha} : {ma} : {se}".format(da = str(D).rjust(2,'0'),ha=str(H).rjust(2,'0'),\
#                                          ma= str(M).rjust(2,'0'),se=str(S).rjust(2,'0')))
#
#
#
#
# ##############
#
#
# def ppp(x):
#     return  str(x).rjust(2,0)
#
# a = 1
#
# ppp(a)
#
#
#
#
