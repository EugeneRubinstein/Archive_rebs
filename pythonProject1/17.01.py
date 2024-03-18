# car = input("Введите буквы машины :")
# n = int(input("Введите буквы машины :"))
# nn = 3
#
# if not car.isalpha():
#     raise TypeError("Должны быть 3 буквы ")
#
#
# if len(car) == 3 and len(n) == nn:
#     print("Старый образец")
# elif len(car) == 4 and len(n) == nn:
#     print("Новый образец")
# else:
#     print("Ощибка вода ")
#
#

#
# a = input()
# if not a.isdigit():
#     raise TypeError("Должны быть 3 буквы ")
# a = [str(i) for i in a]
#
# print(len(a))






#############
# import random
#
#
# win = random.randint(0,36)
#
# cazino = int(input("Введите число :"))
#
#
# if cazino == 37:
#  print("Выпавший номер: 00...")
# else:
#  print("Выпавший номер: %d..." % win)
#
#
# if cazino == 37:
#  print("Выигравшая ставка: 00")
# else:
#  print("Pay", win)
#
#
# if cazino > 37:
#     raise TypeError("Вод только до 36")
#
# if win % 2 == 0:
#     black = "Черное "
# else:
#     black= "Красное "
#
#
#
# if win == 1 or win == 3 or win == 5 or win == 7 or win == 9 or win == 12 or win == 14 or win == 16 or win == 18\
#     or win == 19 or win == 21 or win == 23 or win == 25 or win == 27 or win == 30 or win == 32 or win == 34 or win == 36:
#         chet = "Четное "
# else:
#         chet = "Не Четное "
#
# if win > 18:
#     sh = "От 18 до 36"
# else:
#     sh = "От 0 до 36 "
#
# if win == cazino:
#     uwin = " Вы победили !!!"
# else:
#     uwin = " Вы проиграли !!!"
#
# if cazino == 0:
#     black = ""
#     chet = ""
#     sh = ""
#     cazino = "0"
#     win = "0"
#
#
#
#
#
#
# print("Выпавший номер :", cazino)
# print("Выигравший  стравка :", win)
# print("Выигравший  стравка :", black )
# print("Выигравший  стравка :",chet )
# print("Выигравший  стравка :",sh )
# print(uwin)

# summa = 0
#
# money = input("Введите цену  ( пустая строка для выхода) : ")
#
# while money != "":
#     summa = summa + float(money)
#     money = input("Введите цену  ( пустая строка для выхода) : ")
#
#
#
# print("Общая ваша сума ровняется : ",summa)


#
# x = input("Введите строку х :")
# y = input("Введите строку y :")
#
#
# while x != "":
#     x = input("Введите строку х :")
#     y = input("Введите строку y :")
#

##################

age = int(input("Введите ваш возраст  ( для завершения ведите пустую строку) : "))

if age < 2:
    a = 0
elif age > 3 and age < 12:
    a = 14.00
elif age > 65:
    a = 18.00
elif age > 13 and age < 64:
    a = 23.00



while age != "":
     age = input("Введите ваш возраст  ( для завершения ведите пустую строку) : ")
    if age < 2:
        b = 0
    elif age > 3 and age < 12:
        b = 14.00
    elif age > 65:
        b = 18.00
    elif age > 13 and age < 64:
        b = 23.00
 c = a + b

print(a)






