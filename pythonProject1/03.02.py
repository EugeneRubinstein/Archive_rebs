# import requests
# from pprint import pprint
# from bs4 import BeautifulSoup
# import numpy as np
# a = np.array([1,2,3,4,5,6,7,8,9])
# print(a[[True,True,True,True]])
#
#
#
# # link = "https://browser-info.ru/"
# # resp = requests.get(link).text
# #
# #
# # # with open ("2.html","w",encoding="utf-8") as file:
# # #     file.write(qwer)
# #
# # soup = BeautifulSoup(resp,"lxml")
# # block = soup.find("div", id="tool_padding")
# # js = block.find("div",id="javascript_check")
# # off = js.find_all("span")
# # pprint(off)
# a = 5
# # for i in range(a,0,-1):
# #     print(i)
#
#
# t = "aaabcdaabbaba"
#
# s = set()
# d = {}
#
# for i in range(len(t)-2,-1,-1):
#     d[t[i]] = 100
#     s.add(t[i])
#
#
# print(d)
# print(s)



# b = [-3, 5, 0, -8, 1, 10]
# N = len(b)
#
# for i in range(N-1):
#     m = b[i]
#     p=i
#     for j in range(i+1, N):
#         if m > b[j]:
#             m = b[j]
#             p=j
#     b[i], b[p] = b[p], b[i]
#
# print(b)

# a = [1,2,4,521,341,234,42,54]
# N = len(a)
#
#
# for i in range(1, N):
#     for j in range(i, 0, -1):
#         if a[j] < a[j-1]:
#             a[j], a[j-1] = a[j-1], a[j]
#         else:
#             break
#
# print(a)

#
# t = "данные"
#
#
# S = set()
# M = len(t)
# d= {}
#
#
#
# for i in range(M-2, -1, -1):
#     if t[i] not in S:
#         d[t[i]] = M-i-1
#
#         S.add(t[i])
#
# if t[M-1] not in S:
#     d[t[M-1]] = M
#
# d["*"] = M
#
# print(d)



# class Graph:
#     def __init__(self, num_vertices):
#         self.num_vertices = num_vertices
#         self.adj_list = [[] for _ in range(num_vertices)]
#
#     def add_edge(self, src, dest):
#         self.adj_list[src].append(dest)
#
#     def dfs(self, start):
#         visited = [False] * self.num_vertices
#         stack = [start]
#
#         while stack:
#             vertex = stack.pop()
#             if not visited[vertex]:
#                 print(vertex, end=' ')
#                 visited[vertex] = True
#                 for neighbor in self.adj_list[vertex]:
#                     stack.append(neighbor)
#
# # Создание графа
# g = Graph(4)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)
#
# # Выполнение поиска в глубину
# g.dfs(2)


# a = [[0,3,4,5,],
#      [1,2,1,2,],
#      [1,1,1,1,1]]
# print(len(a))

# a = 4
# b = 5
#
# if a < b:
#     print("asdf")
# else:
#     print("zzz")

# V2 = [[11,22,33,44,51,123,123,123,1,23,1,23],
#      [6,7,8,9,10],
#      [11,12,13,14,15],
#      [16,17,18,19,20],
#      [21,22,23,24]]
#
# V = [[1,2,3,4,5],
#      [6,7,8,9,10],
#      [11,12,13,14,15],
#      [16,17,18,19,20]]
#
#
#
#
#
# N = len(V)
#
#
# P = [[v for v in range(N)] for u in range(N)]
# print(P)


# from collections import deque
#
# def ford_fulkerson(graph, source, sink):
#     flow = 0
#     while True:
#         path, path_flow = bfs(graph, source, sink)
#         if not path:
#             break
#         flow += path_flow
#         update_residual_graph(graph, path, path_flow)
#     return flow
#
# def update_residual_graph(graph, path, flow):
#     for i in range(len(path) - 1):
#         u, v = path[i], path[i + 1]
#         graph[u][v] -= flow
#         graph[v][u] += flow
#
#
# def bfs(graph, source, sink):
#     # 163 декью класс, флоат инк максимальный поток.... сорсе один элемент который будет добавлен в LIFO
#     queue = deque([(source, float('inf'))])
#     parent = {source: None}
#     while queue:
#         node, flow = queue.popleft()
#         for neighbor, capacity in graph[node].items():
#             if neighbor not in parent and capacity > 0:
#                 parent[neighbor] = node
#                 queue.append((neighbor, min(flow, capacity)))
#                 if neighbor == sink:
#                     return (parent, queue[-1][1])
#     return (None, 0)
#
#
# graph = {
#     0: {1: 16, 2: 13},
#     1: {3: 12, 4: 0},
#     2: {1: 10, 4: 14},
#     3: {2: 4, 5: 14},
#     4: {5: 9, 6: 20},
#     5: {4: 7, 6: 4},
#     6: {7: 10}
# }
#
# source = 0
# sink = 7
#
# print(ford_fulkerson(graph, source, sink))
#



# from collections import deque
#
# def ford_fulkerson(graph, source, sink):
#     flow = 0
#     while True:
#         path, path_flow = bfs(graph, source, sink)
#         if not path:
#             break
#         flow += path_flow
#         update_residual_graph(graph, path, path_flow)
#     return flow
#
# def bfs(graph, source, sink): # поиск в ширину делает....проходит начальный потом соседние и до концечной вершины
#     queue = deque([(source, float('inf'))]) # блять , у нас просто список из картежей ... декью клас LIFO, первый это сорс(источник-начало) и макс значения, как на начале
#     parent = {source: None}
#     while queue:
#         node, flow = queue.popleft() # удаляет первое значения .. в нашем случее весь картеж.... если просто в переменую , то там картеж из двух значей ... а если в 2 переменные, то в каждой по значеню
#         for neighbor, capacity in graph[node].items(): # ахуеть , у нас таблица в виде словаря ... и ключи это вершины видимо, и ней это ключ , а кап значения
#             if neighbor not in parent and capacity > 0: # ЕСЛИ ЕГО НЕТ В 228( ЕГО ПЕРВЫЙ РАЗ ВСЕГДА НЕТ, И ЗНАЧЕНИЯ БОЛЬШЕ 0
#                 parent[neighbor] = node # В ЭТУ ЗАЛУПУ ПУСТОЙ СЛОВАРЬ , КИТДАЕТСЯ КЛЮЧ КАК ВЕРШИНЫ ...НОДЕ ЭТО СОРС ТО ЕСТЬ НАЧАЛО
#                 queue.append((neighbor, min(flow, capacity)))
#                 if neighbor == sink:
#                     return (parent, queue[-1][1])
#     return (None, 0)
#
# def update_residual_graph(graph, path, flow):
#     for i in range(len(path) - 1):
#         u, v = path[i], path[i + 1]
#         if u in graph and v in graph[u]:
#             graph[u][v] -= flow
#         if v in graph and u in graph[v]:
#             graph[v][u] += flow
#
# graph = {
#     0: {1: 16, 2: 13},
#     1: {3: 12, 4: 0},
#     2: {1: 10, 4: 14},
#     3: {2: 4, 5: 14},
#     4: {5: 9, 6: 20},
#     5: {4: 7, 6: 4},
#     6: {7: 10}
# }
#
# source = 0
# sink = 7
#
# print(ford_fulkerson(graph, source, sink))
#
#
# a = deque([(1,2),(33,331)])
# b,c = a.popleft()
#
#
# graph2 = {
#     0: {1: 16, 2: 13},
#     1: {3: 12, 4: 0},
#     2: {1: 10, 4: 14},
#     3: {2: 4, 5: 14},
#     4: {5: 9, 6: 20},
#     5: {4: 7, 6: 4},
#     6: {7: 10}
# }
#
#
# print(graph2[0])



#

from collections import deque

# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#
#     while queue:
#         vertex = queue.popleft()
#         if vertex not in visited:
#             visited.add(vertex)
#             queue.extend(graph[vertex] - visited)
#
#     return visited
#
# graph = {
#     'A': set(['B', 'C']),
#     'B': set(['A', 'D', 'E']),
#     'C': set(['A', 'F']),
#     'D': set(['B']),
#     'E': set(['B', 'F']),
#     'F': set(['C', 'E'])
# }
#
# print(bfs(graph, 'A'))


from collections import deque

def bfs(graph, start, target):
    # Используем очередь для хранения узлов, которые нужно посетить
    queue = deque([start])
    # Используем словарь для хранения расстояния от начального узла до каждого узла
    distances = {start: 0}# ////потому что первый элемент может быть 9 , или 5 или А называтся , но по логике он 0 ... потом от него 1 и тд
    # Используем словарь для хранения предков каждого узла
    parents = {start: None}

    while queue:
        # Извлекаем текущий узел из очереди
        current_node = queue.popleft() # .....в эту переменную мы записуем и удаляем первый элемент , начало (1итерация)
        # Если текущий узел является целевым, возвращаем путь к нему
        if current_node == target: # ///// если начало ровно концу ... если 1 = 10 ... на начале такого нет , пох , дальше
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parents[current_node]
            return path[::-1]
        # Иначе, добавляем соседей текущего узла в очередь и обновляем расстояния и предков
        for neighbor in graph[current_node]: # тут у нас в ней ключи  ток ... значений нет
            if neighbor not in distances: # первый раз его нет ... значит сюда ... ключ А его нет в
                distances[neighbor] = distances[current_node] + 1
                parents[neighbor] = current_node
                queue.append(neighbor)
    # Если целевой узел не был найден, возвращаем None
    return None
#
#

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

for i in graph:
    print(i)





# потом мы берем всех соседей у б .... кидаем их в дис ... и даем из значения  по 2 , потому что карент у нас Б, а Б в дис уже есть ... там б 1 ... и тут 2 ... в прошлый раз у нас что было
# у нас в дис дис было А0... и кинули б1с1.... и в родители так же ... теперь родителя, Д Б будет ... обратные
# и тоже самое у нас к Е ... закончили и так же перебираем С с начало и всех его соседей
# перебрали всех до  Ф и у нас dis  = {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 2}///////родители {'A': None, 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'B', 'F': 'C'}, пустая очередь и
#граф {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
# приколюха очереди , что мы можем не ебатся с индексами  ,ставить 3 или три ... а у нас очередь, у нас всегда индекс 0 , и каждый раз новые элементы , она как вспомогательный мув
# у нас выработались родители ... так как мы каждоый раЗ, это числу и ... ставили прошлое число ... из начего мува с очередью ...а там прошлый индекс
# у нас мув работает в 2 второны .. либо работает как его значения 0 ... потом 1 и тд ... либо как его ключ А или ключ всегда преведущий , точнее ток кто в очереди , а там ставят преведущий

# вот мы дошли до конца... у нас очередь это элемент из конца ... значит 376 иф у нас заработает ....вайл работает не много , 3 итерации.... у нас паз ... это переменная в которой будет путь


# в выводе у нас А С Ф , то есть лучше всего из этого дерьма пройти по такому маршруту ...
# пока последний элемент Ф , не равен пустоте ... щас он Ф ... как ток он станет ничем ... Ф не будет .... в путь 379 добовляется Ф
#  и наш каретн, то бишь становится элементом из родителей , с ключем Ф ... то есть у Ф кто родитель ... С .... теперь уже С в путь , и С страновится родителем , то есть А...
# А в список пути ... и А становится родителем , то есть ... у А кто родитель? с самого начала делали А = Нан... и не менялось .. у нее Родитель Нан... и вайл окончен...и принт путь, ток [::-1] значит перевернуть




# d = {1:"0"}
# zzz = {1:"asd",2:"sdf"}
# d["B"] = d[1]
# print(d)
#
#

################################################

# from collections import defaultdict
#
# from collections import defaultdict
#
# graph = {
#     'A': {'B', 'C'},
#     'B': {'D', 'E'},
#     'C': {'F'},
#     'D': set(),
#     'E': {'F'},
#     'F': set()
# }
#
# stack = ['A']
# visited = set()
#
# while stack:
#     current_node = stack.pop()
#     if current_node == 'F':
#         print(True)
#         break
#     if current_node not in visited:
#         visited.add(current_node)
#         stack.extend(graph[current_node] - visited)
# else:
#     print(False)

# def knapsack(weights, values, capacity):
#     n = len(weights)
#     dp = [0 for i in range(capacity + 1)]
#
#
#
#     return dp
#
# weights = [2, 3, 4, 5]
# values = [3, 4, 5, 7]
# capacity = 10
#
# print(knapsack(weights, values, capacity))  # Output: 14


#
# a = [(1,3,4),(1,3,3,3,),(0,54,4,5,)]
# b = sorted(a,key=lambda x:x[0])
# print(b)
# for i in a:
#     print(i)
#
#

# a = {1:"123",2:"5345"}
# a[7].append(66)
# print(a)
#
# a = [1,2,3,1,3,123,1]
# b = min(a)
# print(b)
#
# def get_min(R, U):
#
#
#     rm = (math.inf, -1, -1)
#     for v in U:
#         rr = min(R, key=lambda x: x[0] if (x[1] ==v or x[2] == v) and (x[1] not in U or x[2] not in U) else math.inf
#         if rm[0] > rr[0]:
#
#             rm = rr
#
#
#
#
#
# from functools import reduce
#
# numbers = [1, 2, 3]
#
# def add(x, y):
#     return x - y
#
# result = reduce(add, numbers)
#
# # print(result)  # 15
#
# from cryptography.hazmat.primitives.asymmetric import ec
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.hkdf import HKDF
#
# # Создаем эллиптическую кривую
# curve = ec.SECP256K1()
#
# # Создаем пары ключей для Алисы и Боба
# alice_private_key = curve.generate_private_key()
# alice_public_key = alice_private_key.public_key()
#
# bob_private_key = curve.generate_private_key()
# bob_public_key = bob_private_key.public_key()
#
# # Вычисляем общий секретный ключ
# shared_secret = alice_private_key.exchange(ec.ECDH(), bob_public_key)
#
# # Вычисляем общий секретный ключ
# shared_secret = bob_private_key.exchange(ec.ECDH(), alice_public_key)
#
# # Получаем общий секретный ключ
# shared_secret = HKDF(
#     algorithm=hashes.SHA256(),
#     length=32,
#     salt=None,
#     info=b'handshake data',
# ).derive(shared_secret)
#
# print(f"Общий секретный ключ: {shared_secret}")