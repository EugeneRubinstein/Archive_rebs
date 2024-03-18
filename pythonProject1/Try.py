# bit_8 = int(input("Введите 8 бит : "))
#
#
# a = len((bit_8))
# print(a)
#
# # if len(bit_8) != 8:
# #     raise TypeError("Не обходимо вести 8 цифр")
# #
#
#

#
#
# while bit_8 != '':
#     spisok_bit = [int(i) for i in bit_8]
#
#
#     if spisok_bit[0] != 0 or spisok_bit[0] != 1:
#
#
#         raise TypeError("Не обходимо водить только 0 или 1")
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

# line = input()
# if line.count("0") != 8:
#     raise TypeError
#









#
# message = input("Введите сообщение: ")
# shift = int(input("Введите сдвиг: "))
#
#
#
# for ch in message:
#      if ch >= "a" and ch <= "z":
#
#         pos = ord(ch) - ord("a")
#         pos = (pos + shift) % 26
#         new_char = chr(pos + ord("a"))
#         new_message = new_message + new_char
#
#     elif ch >= "A" and ch <= "Z":
#
#         pos = ord(ch) - ord("A")
#         pos = (pos + shift) % 26
#         new_char = chr(pos + ord("A"))
#         new_message = new_message + new_char
#     else:
#         new_message = new_message + ch
#
# print("Новое сообщение", new_message)

#
# message = input("Введите сообщение: ")
# # shift = int(input("Введите сдвиг: "))



# for ch in message:
#      if ch >= "a" and ch <= "z":
#
#         pos = ord(ch) - ord("a")
#         print(pos)


# a = "alala"
# a = a[1:-1]
#
# print(a)

# palindrop = "a"
# if palindrop[0] == palindrop[-1]:
#     print("а и б одно и тоже ")
# else:
# #     print("не одно и тоже ")
#
#
# MIN = 1
# MAX = 10





#
# for i in range(MIN, MAX + 1):
#  print(i)
#  for j in range(MIN, MAX + 1):
#     print("%4d" % (i * j), end = "")
#  print()

#
# a = "1"
# b = "1"
# print(a+b)
#
#
# def median(a, b, c):
#     if a < b and b < c or a > b and b > c:
#         return b
#     if b < a and a < c or b > a and a > c:
#         return a
#     if c < a and b < c or c > a and b > c:
#         return c
#
#
# def alternateMedian(a, b, c):
#     return a + b + c - min(a, b, c) - max(a, b, c)
#
#
# # Выводим медиану чисел, введенных пользователем
# def main():
#     x = float(input("Введите первое число: "))
#     y = float(input("Введите второе число: "))
#
#     z = float(input("Введите третье число: "))
#     print("Медиана равна:", median(x, y, z))
#     print("С помощью альтернативного метода:", \
#           alternateMedian(x, y, z))
# main()



# def shitly_stish(a):
#     if a == 1:
#         print("shit")
# #     if a == 2:
# #         print("govno")
# #
# #
# # shitly_stish(2)
#
#
# def center(s, width):
#     if width < len(s):
#         return s
#
#     spaces = (width - len(s)) // 2
#     result = " " * spaces + s
#     return result
#
#
# def main():
#     print(center("Известная история", 21))
#     print(center("от:", 8))
# main()

# a = 8 * "a"
# print(a)
# result = result[0: pos] + result[pos].upper() + \
#          result[pos + 1: len(result)]


# a = "asdfasfd sadflkj aswdflkj a i lkjasldkjf i. klasd "
# a = a.split()
# a = a.count("i")
# print(a)
# if pos < len(s):

# def capitalize(s):
#     # Создаем копию исходной строки, в которой будем собирать итоговую строку
#     result = s
#     # Делаем заглавной первый непробельный символ в строке
#     pos = 0
#     while pos < len(s):
#         pos = pos + 1
#         print(pos)
#
# capitalize("asdfasdfasdflkj asdf ")
#
#
# def capitalize(s):
#  # Создаем копию исходной строки, в которой будем собирать итоговую строку
#  result = s
#  # Делаем заглавной первый непробельный символ в строке
#  pos = 0
#  while pos < len(s) and result[pos] == ' ':
#      pos = pos + 1
#      print(result[pos])
#
#
# capitalize("asdfasdfasdflkjw asd kjlaksd j ")

#
#
# result = "asdfafsd"
# result = result[0: 3]
# print(result)
#
#
#
# def capitalize(s):
#     result = s
#     s = result
#
#     pos = 0
#     while pos < len(s) and result[pos] == ' ':
#         pos = pos + 1
#     if pos < len(s):
#
#         result = result[0: pos] + result[pos].upper() + \
#              result[pos + 1: len(result)]
#
# capitalize("asdf sadf ")
#
#
# pos = 0
# while pos < len(s):
#     if result[pos] == "." or result[pos] == "!" or \
#             result[pos] == "?":
#
#             pos = pos + 1
#
# while pos < len(s) and result[pos] == " ":
#     pos = pos + 1
#
# # Если не достигли конца строки, меняем текущий символ на заглавную букву
# if pos < len(s):
#     result = result[0: pos] + \
#              result[pos].upper() + \
#              result[pos + 1: len(result)]
#
# pos = pos + 1
# # Делаем заглавными буквы i, когда им предшествует пробел, а следом идет пробел,
# # точка, восклицательный или вопросительный знак либо апостроф
# pos = 1
# while pos < len(s) - 1:
#     if result[pos - 1] == " " and result[pos] == "i" and \
#             (result[pos + 1] == " " or result[pos + 1] == "." or \
#              result[pos + 1] == "!" or result[pos + 1] == "?" or \
#              result[pos + 1] == "'"):
# # Заменяем i на I, не затрагивая другие символы
# result = result[0: pos] + "I" + \
#          result[pos + 1: len(result)]
# pos = pos + 1
# return result
#
#
# Демонстрируем работу функции
# def main():
#     s = input("Введите текст: ")
#     capitalized = capitalize(s)
#     print("Новая версия:", capitalized)
#
#
# Вызываем основную функцию
# main()




###########################
#
# def capitalize(s):
#     result = s
#     s = result
#
#     pos = 0
#     while pos < len(s) and result[pos] == ' ':
#         pos = pos + 1
#     if pos < len(s):
#
#         result = result[0: pos] + result[pos].upper() + \
#              result[pos + 1: len(result)]
#
# try:
#     result = s
#     s = result
# except NameError("asd"):
#
#
#     pos = 0
# while pos < len(s):
#     if result[pos] == "." or result[pos] == "!" or \
#             result[pos] == "?":
#
#                 pos = pos + 1
# # Пропускаем пробелы
# while pos < len(s) and result[pos] == " ":
#     pos = pos + 1
#
# if pos < len(s):
#     result = result[0: pos] + \
#              result[pos].upper() + \
#              result[pos + 1: len(result)]
#
# pos = pos + 1
#
# pos = 1
# while pos < len(s) - 1:
#     if result[pos - 1] == " " and result[pos] == "i" and \
#             (result[pos + 1] == " " or result[pos + 1] == "." or \
#              result[pos + 1] == "!" or result[pos + 1] == "?" or \
#              result[pos + 1] == "'"):
#         result = result[0: pos] + "I" + \
#                  result[pos + 1: len(result)]
#         pos = pos + 1
#
#        # return result
##################### zzzzzzzzzzz


#
# pos = 0
# result = "hello ciasdf asd i as i"
# s = "hello ciasdf asd i as i"
# def shit(s):
#     pos = 0
#     result = s
#
# while pos < len(s):
#     if result[pos] == "." or result[pos] == "!" or \
#             result[pos] == "?":
#
#             pos = pos + 1
#
# while pos < len(s) and result[pos] == " ":
#     pos = pos + 1
#
# # Если не достигли конца строки, меняем текущий символ на заглавную букву
# if pos < len(s):
#     result = result[0: pos] + \
#              result[pos].upper() + \
#              result[pos + 1: len(result)]
#
# pos = pos + 1
#
# pos = 1
#
#
#
# while pos < len(s) - 1:
#     if result[pos - 1] == " " and result[pos] == "i" and \
#             (result[pos + 1] == " " or result[pos + 1] == "." or \
#             result[pos + 1] == "!" or result[pos + 1] == "?" or \
#             result[pos + 1] == "'"):
#
#                     result = result[0: pos] + "I" + \
#          result[pos + 1: len(result)]
# pos = pos + 1
# print( result)
#
#
# shit("asdfljglkdsfgj  slk j")




################




# a = "basdfh kj"
# pos = 0
# result = a
# b = 1
# while 0 < len(a) and a[0] == " ":
#     print("gigig")
#
# if 0 < len(a):
#     result = result[0: pos] + result[pos].upper() + \
#              result[pos + 1: len(result)]
#
#     print(result)
# #
# pos = 0
# s = "aslkdjf aslkj asdklj . a l jsd ; . Iujaliskdjf ? asdf "
# result = s
# while pos < len(s):
#     if result[pos] == "." or result[pos] == "!" or \
#             result[pos] == "?":
#         pos += 1
#
#     while pos < len(s) and result[pos] == " ":
#         pos = pos + 1
#
#     if pos < len(s):
#         result = result[0: pos] + \
#                  result[pos].upper() + \
#                  result[pos + 1: len(result)]
#


# pos = 0
# s = "wosdf.asdf .asdf?asdf? asdf "
# result = s
# while pos < len(s):
#     if result[pos] == "." or result[pos] == "!" or \
#             result[pos] == "?":
#         pos += 1
#         result = result[0: pos] + \
# #                  result[pos].upper() + \
# #                  result[pos + 1: len(result)]
# #
# #
# #     else:
# #         pos += 1
# #
# # print(result)
#
#
# a = "asfasfd34 "
# z = "asdfafs"
#  = a.strip(z)
# print()
#
#
#
# def isInteger(s):
#
#     s = s.strip()
#
#     if  s[1:].isdigit():
#
#
#             return True
#     else:
#
#             return False
#
#
# a = isInteger("123 4 32")
# print(a)
# import random
# import string
# letters = "1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" + "9" + "0"
# simvol = "!" + "@" + "#" + "$" + ")" + '(' + "*" + "&" + '^' + "%"
# total = string.ascii_letters + simvol
# print(total)
#


# v1 = [1,3,5]
# v2 = [2,4]
#
#
# z = v1[:] = v2
# print(z)
#
#
# try:
#     for i, a in enumerate(v1):
#         v1[i] += v2[i]
# except:
#     print("shot")
# print(v1)


#
# pasw = "AJDDKJ"
#
#
# #
# #     print("yes")
# # else:
#
# #
#     print("yes")
# else:
# if __name__ == '__main__':
#
# # #
# #
# a = "720"
# b = "2"
# for i in a:
#     a = a /b
#     print(i)
# b = 2
# z = 1000
# while True:
#     z = z // b
#     print(z)
#     break z == 1
#
# a = 1000
# for i in range(5):
#     a = a//2
#
#     print(a)



# a = [33,44,643,67456,74657,4356,6,456,45,6]
# for i in a:
#     print(i)
#     print("\n\n")
# print print print print print print print print print print print print print print print print print print print print print print print print print print print print print(print )
# input input input input input
# input input input input input input input input input input input input input input input input input input input unput input input unput input input input input input input
# for for for for for for for for for for for i in for for for for for forf for forforforforforfroforfor for for for for for for for for for for
# for i in for i in for i in for i in for i in for i in for i in for i in for i in for i in for i in for i in range
# A = ((())))(((A = A() ()()()(())))(((((((())))))-----)))))(((((()()(([[[[{{{{}}}}]]]]][[[[]]]]}}}}}}[[[||||||||\\\\\|||||\\\\|||||??????<<<>>>>,,,....<<<>>><><><))))((())))=
# MAIN = PRINT
#
# FIR:
#
# #
# class Link:
#     head = None
#
#     class Node:
#         elememt = None
#         next = None
#
#         def __init__(self,element,next_node = None):
#             self.elememt = element
#             self.next_note = next_node
#
#     def append(self,element):
#         if not self.head:
#             self.head = self.Node(element)
#             return element
#         node = self.head
#
#         while node.next_node:
#             node = node.next_node
#
#         node.next_node = self.Node(element)
#
#     def out(self):
#         node = self.head
#
#         while node.next_node:
#             print(node.elememt)
#             node = node.next_node
#
#
# list = Link()
# list.append(10)
# list.append(101)
# list.append(10312)
#
# list.out()



# print(int("10",2))


# cookies_dict =[
# {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
# for key in session.cookies]
#
# import sys
# a = sys.


# _r = "asdfasdf"
# print(_r)


# import requests
# url = "https://asdf-vm.com/"
# a = requests.get(url).text
# print(a)


# class Lone():
#     def __init__(self,head,nex):
#         self.head = head
#         self.next = nex
#
#
# a = Lone(1,2)
# a = Lone(2,3)
# print(a.__dict__)


import pprint
# class Link:
#     head = None
#
#     class Node:
#
#
#         def __init__(self, element, next_node=None):
#             self.element = element
#             self.next_node = next_node
#
#     def append(self, element):
#         if not self.head:
#             self.head = self.Node(element)
#             return element
#         node = self.head
#
#         while node.next_node:
#             node = node.next_node
#
#         node.next_node = self.Node(element)
#
#     def out(self):
#         node = self.head
#
#         while node:
#             print(node.element)
#             node = node.next_node
#
#     def delete(self, index):
#         if index == 0:
#             self.head = self.head.next_node
#             return
#
#         node = self.head
#         prev_node = None
#
#         while node is not None and index > 0:
#             prev_node = node
#             node = node.next_node
#             index -= 1
#
#         if node is None:
#             return None
#
#         prev_node.next_node = node.next_node
#         element = node.element
#
#         del node
#
#         return "yes"
#
# #
# #
# list = Link()
# list.append(1)
# list.append(2)
# list.append(3)
# list.append(4)
# list.append(5)
# list.delete(2)
# list.out()



# a = [1,2,3]
# b = [1,2]
# a = b
# b[1] = 111
# print(a)



# a = "https://images.pexels.com/photos/2295744/pexels-photo-2295744.jpeq"
# a = a.split(".")
# print(a)


# class Wanga():
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#
# z = Wanga(1,2,3)
# z1 = Wanga(11,22,33)
# z2 = Wanga(111,222,333)
# z.eae = z1
#
# print(z.__dict__)


# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower
#
# class Wheel:
#     def __init__(self, size):
#         self.size = size
#
# class Car:
#     def __init__(self, make, model, engine, wheels):
#         self.make = make
#         self.model = model
#         self.engine = engine
#         self.wheels = wheels
#
# # Создание объектов
# engine = Engine(200)
# wheel1 = Wheel(18)
# wheel2 = Wheel(18)
# wheel3 = Wheel(18)
# wheel4 = Wheel(18)
#
# # Создание объекта Car, который содержит другие объекты
# car = Car("Toyota", "Corolla", engine, [wheel1, wheel2, wheel3, wheel4])
#
# # Вывод информации о машине
# print(f"Make: {car.make}")
# print(f"Model: {car.model}")
# print(f"Engine horsepower: {car.engine.horsepower}")
# print(f"Wheel size: {car.wheels[0].size}")
# pprint.pprint(car.__dict__)



# def a (stroka):
#     return stroka
#
#
# aa = a("qwerqwer")
# print(aa)
# vop = input(":::")
# vop2 = input("^^^^")
# bb = a(stroka=f"{vop}/page{vop2}/")
# print(bb)
# z = [1,2,3,4,5,6]
# a = [1,2,3,4,5,6]
# a = z
# b = [999,888,777]
# a.insert(3,b)
# print(a)
# print(z)
#
#
# response = requests.get(SITE, prox1es=None)
# extension = response.headers["content-type"].split("/")[-1]



# class Node:
#     def __init__(self, element, next_node=None, previous_node=None):
#         self.element = element
#         self.next_node = next_node
#         self.previous_node = previous_node
#
# class DblList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
#
#     def add(self, element):
#         if not self.head:
#             self.head = Node(element)
#             self.tail = self.head
#         else:
#             new_node = Node(element, None, self.tail)
#             self.tail.next_node = new_node
#             self.tail = new_node
#         self.length += 1
#
#     def display(self):
#         current = self.head
#         while current:
#             print(current.element, end=" ")
#             current = current.next_node
#         print()
#
# # Тестируем нашу реализацию
# my_list = DblList()
# my_list.add(1)
# my_list.add(2)
# my_list.add(3)
# my_list.add(4)
# my_list.add(4)
# my_list.add(4)
# my_list.display()  # Выведет: 1 2 3 4



# class Node:
#     def __init__(self, element, next_node=None, previous_node=None):
#         self.element = element
#         self.next_node = next_node
#         self.previous_node = previous_node
#
# class DblList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
#
#     def add(self, element):
#         if not self.head:
#             self.head = Node(element)
#             return element
#         elif not self.tail:
#             self.tail = Node(element,None,self.head)
#             self.head.next_node = self.tail
#             return element
#         else:
#             self.tail = Node(element,None,self.tail)
#             self.tail.previous_node.next_node = self.tail
#             return element
#
#
#     def displayy(self):
#         current = self.head
#         while current:
#             print(current.element, end=" ")
#             current = current.next_node
#         print()
#
# # Тестируем нашу реализацию
# my_list = DblList()
# my_list.add(1)
# my_list.add(2)
# my_list.add(3)
# my_list.add(4)
# my_list.add(4)
# my_list.add(4)
# my_list.displayy()  # Выведет: 1 2 3 4
#
#

# class DblList:
#
#
#     class Node:
#
#
#         previous_node = None
#         next_node = None
#         element = None
#
#
#         def __init_(self, element, next_node=None, previous_node=None) -> None:
#
#
#             self.element = element
#             self.next_node = next_node
#             self.previous_node = previous_node
#
#
#     head = None
#     tail = None
#     length = 0
#
#
#
#     def add(self, element):
#
#
#         if not head:
#             self.head = self.Node(element)
#             return element
#
#         elif not tail:
#             self.tail = self.Node(element, None, self.head)
#             self.head.next_node = self.tail
#             return element
#
#         else:
#
#              self.tail = self.Node(element, None, self.tail)
#              self.tail.previous_node.next_node = self.tail
#              return element
#
# ap = DblList()
# ap.add(1)
# ap.add(2)
# ap.add(3)
# ap.add(4)


# class DblList:
#     class Node:
#         def __init__(self, element, next_node=None, previous_node=None):
#             self.element = element
#             self.next_node = next_node
#             self.previous_node = previous_node
#
#     head = None
#     tail = None
#     length = 0
#
#     def add(self, element):
#         if not self.head:
#             self.head = self.Node(element)
#             self.tail = self.head
#         else:
#             new_node = self.Node(element, None, self.tail)
#             self.tail.next_node = new_node
#             self.tail = new_node
#         self.length += 1
#
# # Тестируем нашу реализацию
# my_list = DblList()
# my_list.add(1)
# my_list.add(2)
# my_list.add(3)
# my_list.add(4)



# class Nore:
#     def __init__(self,a):
#         self.a = a
#
# z = Nore(111)
# zz = Nore(1131)
# zzz = Nore(11441)
# for i in z:
#     print(i)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node:
            elements.append(cur_node.data)
            cur_node = cur_node.next
        return elements

    def delete(self, data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                if cur_node.prev:
                    cur_node.prev.next = cur_node.next
                if cur_node.next:
                    cur_node.next.prev = cur_node.prev
                if cur_node == self.head:
                    self.head = cur_node.next
                return
            cur_node = cur_node.next

    def insert(self, data, index):
        if index < 0 or index > self.length():
            return "Index out of range"
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            cur_node = self.head
            cur_index = 0
            while cur_index < index - 1:
                cur_node = cur_node.next
                cur_index += 1
            new_node = Node(data)
            new_node.prev = cur_node
            new_node.next = cur_node.next
            cur_node.next.prev = new_node
            cur_node.next = new_node

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
print(dll.display())  # [1, 2, 3, 4, 5]
dll.insert(0, 0)
print(dll.display())  # [0, 1, 2, 3, 4, 5]
dll.insert(6, 5)
print(dll.display())  # [0, 1, 2, 3, 4, 6, 5]
dll.delete(3)
print(dll.display())  # [0, 1, 2, 4, 6, 5]