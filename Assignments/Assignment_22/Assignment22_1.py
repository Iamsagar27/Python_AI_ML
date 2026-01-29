class Demo:
    Value = 0

    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def Fun(self):
        print("Instance Variable from Fun :", self.no1, self.no2)

    def Gun(self):
        print("Instance Variable from Gun :", self.no1, self.no2)

Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Obj1.Fun()
Obj2.Fun()

Obj1.Gun()
Obj2.Gun()