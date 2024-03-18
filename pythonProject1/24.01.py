# def capitalize(s):
#     # Создаем копию исходной строки, в которой будем собирать итоговую строку
#     result = s
#     # Делаем заглавной первый непробельный символ в строке
#     pos = 0
#     while pos < len(s) and result[pos] == ' ':
#         pos = pos + 1
#
#     if pos < len(s):
#         result = result[0: pos] + result[pos].upper() + \
#                  result[pos + 1: len(result)]
#
#
#
#
#     pos = 0
#
#     while pos < len(s):
#         if result[pos] == "." or result[pos] == "!" or \
#              result[pos] == "?":
#             pos += 1
#             result = result[0: pos] + \
#                     result[pos].upper() + \
#                     result[pos + 1: len(result)]
#
#
#         else:
#             pos += 1
#
#
#
#
#
#     pos = 1
#     while pos < len(s) - 1:
#         if result[pos - 1] == " " and result[pos] == "i" and \
#                 (result[pos + 1] == " " ):
#
#                 result = result[0: pos] + "I" + \
#              result[pos + 1: len(result)]
#         else:
#             pos = pos + 1
#     return result
#
# b = capitalize("смотри тут есть текст .тут тоже .ттож ?а i i i i asdf i ")
# print(b)



# a, b = map(int,input().split())
#
# print(a,b)


# def div(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "деление на ноль"
#
#
# try:
#     x, y = 1, 2
#     res = div(x, y)
#
# except ValueError as z:
#     print(z)
#
#
# print(res)

# целочисленное знаечение .... типо 1,5,7... тру выдимо на выходе ... хз что , но типо просто это целое или не целое инт
# пробелы убрать при вооде ... когда потом будлет без пробелов 12879498718432

# isInteger("asdf234 sdf a345 2w as")

#
# a = "asdf23498"
# print(a.isalpha())
#
#
# string = "Пример 123 строки 456 с числами."
# numbers = ''.join(i for i in string if i.isdigit())
# print(numbers)
#
#
# a = "asdf132"
# b = "".join(i for i in a if i.isalpha())
# print(b)




# import string
# def isInteger(s :str):
#     taby = string.ascii_letters
#     taby  = " " + taby
#     print(taby)
#     s = s.strip(taby)
#     print(s)
#
#
# isInteger("234 234 44")
#



# def isInteger(s :str):
#    s = s.split()
#    a = map(s,abc)
#
# isInteger("12 12 321 ")

# a = input()
# a = [int(i) for i in a]
# print(a)


# a = 4
# b = [3,5]
# b.isdigit()

#
# def isInteger(s):
#     s = s.strip()
#
#     if (s[0] == "+" or s[0] == "–") and s[1:].isdigit():
#
#         print("yes",s)
#     else:
#         print("not")
#
#
# a = isInteger("+2 34")
#
# print(a)
#
# def isInteger(s :str):
#
#     digit = "".join(i for i in s if i.isdigit())
#     if digit.isdigit():
#         print("Целочисленное, ")
#     else:
#         print("Не Целочисленое ")
# #
#
#
# def main():
#     s = input("Введите строку: ")
#     isInteger(s)
#
# main()


# def pristoe_chislk(n):
#
#         if n <= 1:
#             return False
#
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True
#
#
# def main():
#     value = int(input("Введите целое число: "))
#     if pristoe_chislk(value):
#         print(value, "– простое число.")
#     else:
#         print(value, "не является простым числом.")

import random
import string


# def password():
#     letters = "1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" + "9" + "0"
#     simvol = "!" + "@" + "#" + "$" + ")" + '(' + "*" + "&" + '^' + "%"
#     total = string.ascii_letters + simvol + letters
#
#     a = random.choice(total)
#     b = random.choice(total)
#     c = random.choice(total)
#     d = random.choice(total)
#     f = random.choice(total)
#     g = random.choice(total)
#     h = random.choice(total)
#     n = random.choice(total)
#     m = random.choice(total)
#     l = random.choice(total)
#     pass_word = a + b + c + d + f + g + h + n + m + l
#
#     return print(pass_word)
#
#
# password()


# def password():
#     letters = "1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" + "9" + "0"
#     simvol = "!" + "@" + "#" + "$" + ")" + '(' + "*" + "&" + '^' + "%"
#     total = string.ascii_letters + simvol + letters
#
#     a = random.choice(total)
#     b = random.choice(total)
#     c = random.choice(total)
#     d = random.choice(total)
#     f = random.choice(total)
#     g = random.choice(total)
#     h = random.choice(total)
#     n = random.choice(total)
#     m = random.choice(total)
#     l = random.choice(total)
#     pass_word10 = a + b + c + d + f + g + h + n + m + l
#     pass_word9 = a + b + c + d + f + g + h + n + m
#     pass_word8 = a + b + c + d + f + g + h + n
#     pass_word7 = a + b + c + d + f + g + h
#     shit = random.choice([pass_word7,pass_word8,pass_word9,pass_word10])
#     return shit
#
#
# def main ():
#     print("Ваш случайный пароль ", password())
#
# if __name__ == '__main__':
#     main()

#
# from random import randint
#
#
# def randomPassword():
#     """Функция для создания пароля из 7-10 случайных символов"""
#     randomLength = randint(7, 10)
#
#     result = ""
#     for i in range(randomLength):
#         randomChar = chr(randint(33, 126))
#         result = result + randomChar
#
#     return result
#
#
# def main():
#     print("Ваш случайный пароль:", randomPassword())
#
#
# if __name__ == "__main__":
#     main()





# class Meta(type):
#     def create(self,*args,**kwargs):
#         for key,value in self.class_ar.items():
#             self.__dict__[key] = value
#
#
#
#     def __init__(cls,name,beses,attrs):
#         cls.class_ar = attrs
#         cls.__init__ = Meta.create
# class Pox(metaclass=Meta):
#     a = "asdf"
#     b = "asdfgg"
#     c = "a123sdf"
#
#
# z = Pox()
# print(z.__dict__)


# def check_password(pasword):
#     """Проверка пароля на надежность(больше 8 символов,+1цифра,+ 1 буква = верхний или нижний регистр """
#
#     if len(pasword) > 8 and  pasword.count("1") or pasword.count("2") or pasword.count("3") or pasword.count("4") or pasword.count("5") or pasword.count("6") or \
#             pasword.count("7") or pasword.count("8") or  pasword.count("9") or  pasword.count("0"):
#         return True
#     else:
#         return False
#
#
# def main():
#     question = input("Введите ваш пароль : ")
#     print("Надежность вашего пароля : ", check_password(question))
#
#
# if __name__ == "__main__":
#     main()



# def check_password(pasword):
#     """Проверка пароля на надежность(больше 8 символов,+1цифра,+ 1 буква = верхний или нижний регистр """
#     numbers = "".join(i for i in pasword if i.isdigit())
#     if len(pasword) > 8 and len(numbers) >= 1 :
#
#        return True
#     else:
#         return False
#
#
# def main():
#     question = input("Введите ваш пароль : ")
#     print("Надежность вашего пароля : ", check_password(question))
#
#
# if __name__ == "__main__":
#     main()
#
# def check_password(pasword):
#     """Проверка пароля на надежность(больше 8 символов,+1цифра,+ 1 буква = верхний или нижний регистр """
#     numbers = "".join(i for i in pasword if i.isdigit())
#     if not pasword.isupper():
#
#        return True
#     else:
#         return False
#
#
# def main():
#     question = input("Введите ваш пароль : ")
#     print("Надежность вашего пароля : ", check_password(question))
#
# print(check_password)
# # if __name__ == '__main__':
# #     main()



# a = "asd"
#
# while a:
#     print("asdf")
#

class A:
    __instance = None
    