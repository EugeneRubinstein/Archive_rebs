# BABY_PRICE = 0.00
# CHILD_PRICE = 14.00
# ADULT_PRICE = 23.00
# SENIOR_PRICE = 18.00
#
# BABY_LIMIT = 2
# CHILD_LIMIT = 12
# ADULT_LIMIT = 64
#
# total = 0
# # Читаем ввод пользователя до пустой строки
# age = input("Введите возраст посетителя (пустая строка для окончания ввода): ")
# while age != "":
#  age = str(age)
#
#  if age == "asd":
#     total = "asdfasdf"
#  elif age == "asdaa":
#     total = "asdfasdf"
#  elif age == "asda":
#     total = "asdfasdf"
#
#  # Считываем возраст следующего посетителя
#  line = input("Введите возраст посетителя (пустая строка для окончания ввода): ")
# # Отображаем сумму группового посещения с правильным форматированием
# print("Сумма посещения зоопарка для этой группы составит $%.2f" % total)
#
#

#
# #
# BABY_LIMIT = 2
# CHILD_LIMIT = 12
# ADULT_LIMIT = 64
#
# total = 0
# # Читаем ввод пользователя до пустой строки
# line = int(input("Введите возраст посетителя (пустая строка для окончания ввода): "))
# while line != "":
#  age = int(line)
#
#  if age <= BABY_LIMIT:
#     total = total + 0
#  elif age <= CHILD_LIMIT:
#     total = total + 14.00
#  elif age <= ADULT_LIMIT:
#     total = total + 23.00
#  else:
#     total = total + 18.00
#  # Считываем возраст следующего посетителя
#  line = input("Введите возраст посетителя (пустая строка для окончания ввода): ")
# # Отображаем сумму группового посещения с правильным форматированием
# print("Сумма посещения зоопарка для этой группы составит $%.2f" % total)

########
#



#
#     #деление по модулю
#

#
# a = [1,3,55,66,7]
# print(sum(a))
#
#
# a = input()
# a = [int(i) for i in a]
# # print(sum(a))
# #
# # #####
#
# bit_8 = input("Введите 8 бит : ")
#
# if len(bit_8) != 8:
#     raise TypeError("Не обходимо вести 8 цифр")
#
#
#
#
#
#
# while bit_8 != '':
#     spisok_bit = [int(i) for i in bit_8]
#
#
#     # if spisok_bit[0] != 0 or spisok_bit[0] != 1 and \
#     #         spisok_bit[1] != 0 and spisok_bit[1] != 1 and \
#     #         spisok_bit[2] != 0 and spisok_bit[2] != 1 and \
#     #         spisok_bit[3] != 0 and spisok_bit[3] != 1 and \
#     #         spisok_bit[4] != 0 and spisok_bit[4] != 1 and \
#     #         spisok_bit[5] != 0 and spisok_bit[5] != 1 and \
#     #         spisok_bit[6] != 0 and spisok_bit[6] != 1 and \
#     #         spisok_bit[7] != 0 and spisok_bit[7] != 1:
#     #     raise TypeError("Не обходимо водить только 0 или 1")
#
#
#
#
#
#     if sum(spisok_bit) % 2:
#         bit = 1
#     else:
#         bit = 0
#
#     print("Бит четности равен :",bit)
#     bit_8 = input("Введите 8 бит : ")
#
#
#
# #
# # bit_8 = input("Введите 8 бит : ")
# # while bit_8 != '':
# #     spisok_bit = [int(i) for i in bit_8]
# #     if spisok_bit[0] != 0 and spisok_bit[0] != 1 and spisok_bit[1] != 0 and spisok_bit[1] != 1:
# #         raise TypeError("aaaaaaaaaa")
# #
# #     print(spisok_bit)
# #     bit_8 = input("Введите 8 бит : ")
#


# line = input("Введите 8 бит информации: ")
#
# while line != "":
#
#  if line.count("0") + line.count("1") != 8 or len(line) != 8:
#
#     print("Это не 8 бит… Попробуйте еще.")
#  else:
#
#     ones = line.count("1")


# line = input("asdasd^^^")
# ones = line.count("1")
# print(ones)

############

# import string
# a = string.ascii_letters
# salat = input("Введите фразу ")
# sdvig = input("Количество символов для сбвига ")
#
#
# if salat == "a":
#
# print(a[3])
a = chr (97)
print(a)