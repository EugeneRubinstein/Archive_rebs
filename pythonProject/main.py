class Cat:
    a = None
    b = None
    c = None

    def set_data(self,a, b ,c ):
        self.a = a
        self.b = b
        self.c = c




cat1 = Cat()

cat1.set_data(3, 5 ,8)
cat1.a = "asdfa"


print(cat1.b)