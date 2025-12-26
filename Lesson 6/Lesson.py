class Point:
    """"For creation and set coords"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def check_coords(self):
        for attr in self.__dict__:
            if getattr(self, attr,False) < 0:
                print("Coord can't be negative")
                setattr(self, attr, 0)
            elif getattr(self, attr,False) > 100:
                print("Coord can't be greater than 100")
                setattr(self, attr, 100)
        print(self.__dict__)
    def get_attrs(self):
        print(self.__dict__)

    def set_attrs(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(self.__dict__)

coord_1 = Point(-1, 101, 50)
coord_1.get_attrs()
coord_1.check_coords()