# palindrop = input("Введите строку :")
# # palindrop = "alalala"
#
#
#
# # в вайл условие для остановки веди
# while len(palindrop) != 1:
#     if palindrop[0] == palindrop[-1]:
#         palindrop = palindrop[1:-1]
#         done = "Это Полиндроп"
#
#     else:
#         done = "Это не палиндроп"
#         break
#
# print(done)
#
#
# for z in range(1,11):
#     print(z,end=" ")
#
# print(" ")
# for i in range(1, 11):
#     print(i, end=" ")
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print()





# 99 / 3 = 3.... not 3 ,,,, 33 ////33
# 120 this 2/60
#200/100


# n = int(input("Введите положительное число :"))
# m = int(input("Введите второе положительное число :"))
#
# if n  % 2 == 0 and m % 2 == 0:
#     d = 2
# elif n  % 3 == 0 and m % 3 == 0:
#     d = 3
# elif n  % 4 == 0 and m % 4 == 0:
#     d = 4
# elif n  % 5 == 0 and m % 5 == 0:
#     d = 5
# elif n  % 6 == 0 and m % 6 == 0:
#     d = 6
# else:
#     d = 1
#
#
# if n % d == 0 and m % d == 0:
#  d += 1
#
#  print(d)

#
# n = int(input("Введите первое целое число: "))
# m = int(input("Введите второе целое число: "))
#
# d = min(n, m)
#
# while n % d != 0 or m % d != 0:
#     d = d - 1
#
# print(d)
# a = [1,2,3,4]
# z = a.pop()
# print(a,z)


# def summa(a,b,c):
#     return a + b + c
#
# a, b ,c = summa(1,2,3)
# print(a,b,c)


class Node:


    def __init__(self, data):


        self.data = data
        self.left = self.right = None


class Tree:


    def __init__(self):


        self.root = None


    def __find(self, node, parent, value):

        if node is None:
            return None, parent, False


        if value == node.data:
            return node,parent,True


        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
            else:
                return None, None


        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False


    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return  obj


    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)



v = [10,5,7,16,13,2,20]

t = Tree()
for x in v:
    t.append(Node(x))