# rezult = " "
# b = 2
# q = input("Введите число : ")
#
# while True:
#     r = int(q) % b
#     rezult = r + str(r)
#     q = int(q) // 2
#     print(r)
#
#
import random
# # max = random.randint (1,100)
#
#
# b = []
#
#

#
#
# print('Максимальное значение в ряду:',max(b))
#
#
# b.sort()
# print(b[99],"<== Обновление")
# print(b[98],"<== Обновление")
# print(b[97],"<== Обновление")
# print(b[96],"<== Обновление")
# print(b[95],"<== Обновление")
#



# лмбо еще + 99 а ..... лиюо рандж 99 .....какую то проверку потом

#
# for i in range(100):
#     a = random.randrange(10,22,6)
#     print(a)


# for i in range(100):
#     a = random.randint(1, 99)
#     print(a)
#
#
# from random import randrange
#
# NUM_ITEMS = 100
#
# mx_value = randrange(1, NUM_ITEMS + 1)
# print(mx_value)
#
# num_updates = 0
#
# for i in range(1, NUM_ITEMS):
#     # Генерируем новое случайное число
#     current = randrange(1, NUM_ITEMS + 1)
#
#     if current > mx_value:
#
#     mx_value = current
#     num_updates = num_updates + 1
#     # Отображаем значение с пометкой
#     print(current, "<== Обновление")
#     else:
#         print(current)
#
# print("Максимальное значение в ряду:", mx_value)
# print("Количество смен максимального значения:", num_updates)



# aa = int(input("Введите первое число :"))
# bb = int(input("Введите второе число :"))
# cc = int(input("Введите третье число :"))
# #

# def miraj(a,b,c):
#     midle = max(a,b,c) - min(a,b,c)
#     return midle
# bbb = miraj(aa,bb,cc)
# print(bb)
#


# def miraj(a,b,c,spisok=[]):
#     spisok.append(a)
#     spisok.append(b)
#     spisok.append(c)
#     spisok.sort()
#     return spisok[1]
#
#
# a = miraj(aa,bb,cc)
# print(a)




def miraj(*args,spisok=[]):
    spisok.append(*args)
    spisok.sort()

    return spisok


a = miraj(22,33,66)
print(a)


def miraj(a,b,c,spisok=[]):
    spisok[0] = a
    spisok[1] = b
    spisok[2] = c
    if True:
        try:
            return spisok
        except:
            pass


a = miraj(1,55,77)

print(a)