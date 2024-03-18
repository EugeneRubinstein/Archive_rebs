# # # # # class Node:
# # # # #
# # # # #
# # # # #     def __init__(self, data):
# # # # #
# # # # #
# # # # #         self.data = data
# # # # #         self.left = self.right = None
# # # # #
# # # # #
# # # # # class Tree:
# # # # #
# # # # #
# # # # #     def __init__(self):
# # # # #
# # # # #
# # # # #         self.root = None
# # # # #
# # # # #     def __find(self, node, parent, value):
# # # # #         if value < node.data:
# # # # #             if node.left:
# # # # #                 return self.__find(node.left, node, value)
# # # # #             else:
# # # # #                 return None, None, None
# # # # #
# # # # #         if value > node.data:
# # # # #             if node.right:
# # # # #                 return self.__find(node.right, node, value)
# # # # #             else:
# # # # #                 return None, None, None
# # # # #
# # # # #         return node, parent, True
# # # # #
# # # # #
# # # # #     def append(self, obj):
# # # # #         if self.root is None:
# # # # #             self.root = obj
# # # # #             return obj
# # # # #
# # # # #         s, p , fl_find = self.__find(self.root, None, obj.data)
# # # # #
# # # # #         if not fl_find and s:
# # # # #             if obj.data < s.data:
# # # # #                 s.left = obj
# # # # #             else:
# # # # #                 s.right = obj
# # # # #
# # # # #         return  obj
# # # # #
# # # # #
# # # # #     def show_tree(self, node):
# # # # #         if node is None:
# # # # #             return
# # # # #
# # # # #         self.show_tree(node.left)
# # # # #         print(node.data)
# # # # #         self.show_tree(node.right)
# # # # #
# # # # #
# # # # #
# # # # # v = [10,5,7,16,13,2,20]
# # # # #
# # # # # t = Tree()
# # # # # for x in v:
# # # # #     t.append(Node(x))
# # # # #
# # # # # t.show_tree(t.root)
# # # # #
# # # # #
# # # class Node:
# # #     def __init__(self, data):
# # #         self.data = data
# # #         self.left = None
# # #         self.right = None
# # #
# # # class Tree:
# # #     def __init__(self):
# # #         self.root = None
# # #
# # #     def __find(self, node, parent, value):
# # #
# # #
# # #
# # #         if value < node.data:
# # #             if node.left:
# # #                 return self.__find(node.left, node, value)
# # #
# # #
# # #         if value > node.data:
# # #             if node.right:
# # #                 return self.__find(node.right, node, value)
# # #
# # #
# # #         return node, parent, False
# # #
# # #     def append(self, obj):
# # #         if self.root is None:
# # #             self.root = obj
# # #             return obj
# # #
# # #         s, p , fl_find = self.__find(self.root, None, obj.data)
# # #
# # #         if not fl_find and s:
# # #             if obj.data < s.data:
# # #                 s.left = obj
# # #             else:
# # #                 s.right = obj
# # #
# # #         return  obj
# # #
# # #     def show_tree(self, node):
# # #         if node is None:
# # #             return
# # #
# # #         self.show_tree(node.left)
# # #         print(node.data)
# # #         self.show_tree(node.right)
# # #
# # #
# # # v = [10, 55, 7, 16, 13, 2, 20]
# # #
# # # t = Tree()
# # # for x in v:
# # #     t.append(Node(x))
# # #
# # # t.show_tree(t.root)
# # # #
# # # #
# # # # #
# # # # # def a (a,z):
# # # # #     aa = a + z
# # # # #     aaa = a * z
# # # # #     zzz = a * a
# # # # #     return aa, aaa, zzz, True
# # # # #
# # # # #
# # # # # r,t,y,m = a(1,2)
# # # # #
# # # # # print(m)
# # #
# # #
# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.left = None
# #         self.right = None
# #
# # class Tree:
# #     def __init__(self):
# #         self.root = None
# #
# #     def __find(self, node, parent, value):
# #         if node is None:
# #             return None, parent, False
# #
# #         if value < node.data:
# #             if node.left:
# #                 return self.__find(node.left, node, value)
# #             else:
# #                 return node, parent, False
# #
# #         if value > node.data:
# #             if node.right:
# #                 return self.__find(node.right, node, value)
# #             else:
# #                 return node, parent, False
# #
# #         return node, parent, False
# #
# #
# #
# #     def append(self, obj):
# #         if self.root is None:
# #             self.root = obj
# #             return obj
# #
# #         s, p , fl_find = self.__find(self.root, None, obj.data)
# #
# #         if not fl_find and s:
# #             if obj.data < s.data:
# #                 s.left = obj
# #             else:
# #                 s.right = obj
# #
# #         return  obj
# #
# #     def show_tree(self, node):
# #         if node is None:
# #             return
# #
# #         self.show_tree(node.left)
# #         print(node.data)
# #         self.show_tree(node.right)
# #
# #
# # v = [10, 55, 7, 16, 13, 2, 20]
# #
# # t = Tree()
# # for x in v:
# #     t.append(Node(x))
# #
# # t.show_tree(t.root)
# #
# #
# # from collections import OrderedDict
# #
# # d = OrderedDict()
# # d[1] = "one"
# # d[3] = "three"
# # d[2] = "two"
# #
# # for k, v in d.items():
# #     print(k, v)
#
# #
# # print(chr(33))
#
#
# class HashTable:
#     def __init__(self):
#         self.size = 10
#         self.table = [None] * self.size
#
#     def hash_function(self, key):
#         return key % self.size
#
#     def insert(self, key, value):
#         index = self.hash_function(key)
#         if self.table[index] is None:
#             self.table[index] = LinkedList()
#         self.table[index].insert(key, value)
#
#     def search(self, key):
#         index = self.hash_function(key)
#         if self.table[index] is None:
#             return None
#         else:
#             return self.table[index].search(key)
#
#     def delete(self, key):
#         index = self.hash_function(key)
#         if self.table[index] is None:
#             return None
#         else:
#             return self.table[index].delete(key)
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert(self, key, value):
#         if self.head is None:
#             self.head = Node(key, value)
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = Node(key, value)
#
#     def search(self, key):
#         current = self.head
#         while current is not None:
#             if current.key == key:
#                 return current.value
#             current = current.next
#         return None
#
#     def delete(self, key):
#         if self.head is None:
#             return None
#         elif self.head.key == key:
#             self.head = self.head.next
#         else:
#             current = self.head
#             while current.next is not None:
#                 if current.next.key == key:
#                     current.next = current.next.next
#                     return
#                 current = current.next
#
# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None


a = [1,2,3,4,5,6]
b = a.pop()
print(a)