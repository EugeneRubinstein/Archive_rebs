class Geom:
    name = "geom"

    def __init__(self, x1, x2, y1, y2):
        print("Geommmm")
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Line(Geom):





class Rect(Geom):
    def __init__(self, x1, x22, y1, y2,ppp = None,fill = None):
        print("Recttt")
        self.fill = fill
        self.ppp = ppp




print(l.__dict__)
print(r.__dict__)




