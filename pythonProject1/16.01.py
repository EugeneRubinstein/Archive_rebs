# Score = input("Введите оценку :").upper()
#
#
#
# if Score == "A+":
#     number = 4.0
# elif Score == "A":
#     number = 4.0
# elif Score == "A-":
#     number = 3.7
# elif Score == "B+":
#     number = 3.3
# elif Score == "B":
#     number = 3
# elif Score == "B-":
#     number = 2.7
# elif Score == "C+":
#     number = 2.3
# elif Score == "C":
#     number = 2
# elif Score == "C-":
#     number = 1.7
# elif Score == "D+":
#     number = 1.3
# elif Score == "D-":
#     number = 1
# elif Score == "F":
#     number = 0
# else:
#     print("Не правильный вод")
#
#
# print("Ваша оценка в числе будет состовлять",number)


# #########
# rating = float(input("Введите ваш рейтинг :"))
#
# lil = 0.0
# middle = 0.4
# high = 0.6
# a = 0.5
#
#
# prize = 2400.00
#
#
# if rating == lil:
#     print("Ваш рейтинг является низким. Ваша премия состовляет : 0.0 ")
#
# elif rating == middle :
#     prize_2 = prize * middle
#     print("Ваш рейтинг является средним. Ваша премия состовляет :  ",prize_2," долларов")
#
# elif rating == 0.5 :
#     prize_5 = prize * a
#     print("Ваш рейтинг является средним. Ваша премия состовляет :  ",prize_5," долларов")
#
# elif rating == high:
#     prize_3 = prize * high
#     print("Ваш рейтинг является высоким .Ваша премия состовляет :  ",prize_3," долларов")
#
# elif rating > 0.7:
#     prize_4 = prize * rating
#     print("Ваш рейтинг является высоким .Ваша премия состовляет :  ",prize_4," долларов")
# else:
#     print("Не правильный вод ")

#
# year = int(input("Введите год :"))
#
# ostatok = year % 400
# ostatok2 = ostatok % 100
#
#
#
# if year % 400 == 0:
#     print("Высокостный")
# elif ostatok % 100 == 0:
#     print("Не высокостный")
# elif ostatok2 % 4 == 0:
#     print("Высокостный ")
# else:
#     print(" Не высокостный ")



#
# year = int(input("Введите год :"))
#
#
# if year % 400 == 0:
#     print("Высокостный")
# elif year % 100 == 0:
#     print("Не высокостный")
# elif year % 4 == 0:
#     print("Высокостный ")
# else:
#     print(" Не высокостный ")



# car = input("Введите буквы машины :")
# car_numbers = int(input("Введите номер машины :"))
# a = 3
# b = 3
# if not car.isalpha():
#     raise TypeError("Должны быть 3 буквы ")
#
# if len(car) == a and car_numbers == b:
#     print("У вас старый формат машины ")
# elif len(car) == a and car_numbers == b:
#     print("У вас новый формат машины ")


#
# number = input("Введите номер машины :").upper()
#
# if len(number) == 6 and \
#     number[0] >= "A" and number[0] <= "Z" and \
#     number[1] >= "A" and number[1] <= "Z" and \
#     number[2] >= "A" and number[2] <= "Z" and \
#     number[3] >= "0" and number[3] <= "9" and \
#     number[4] >= "0" and number[4] <= "9" and \
#     number[5] >= "0" and number[5] <= "9" :
#         print("Это номер старого образца")
# elif len(number) == 7 and \
#     number[0] >= "A" and number[0] <= "Z" and \
#     number[1] >= "A" and number[1] <= "Z" and \
#     number[2] >= "A" and number[2] <= "Z" and \
#     number[3] >= "0" and number[3] <= "9" and \
#     number[4] >= "0" and number[4] <= "9" and \
#     number[5] >= "0" and number[5] <= "9" and \
#     number[6] >= "0" and number[6] <= "9":
#         print("Это номер нового образца")












