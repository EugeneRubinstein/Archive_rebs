class Node(object):

    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next


    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class Link():
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node == None:
            self.head == new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)



    def show(self):
        cur_node = self.head
        output = ""
        while cur_node != None:
            output += str(cur_node.get_data()) + " -> "
            cur_node = cur_node.get_next()
        print(cur_node)



my_list = Link()

my_list.append(2)
my_list.append(4)
my_list.append(8)
my_list.append(16)
my_list.show()



class Node(object):

    def __init__(self,data , next ):
        self.data = data
        self.next = next


    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class Link():
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)
        print(new_node)


a = Link()
a.append(11)






