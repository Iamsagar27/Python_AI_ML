class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0
        self.Area = 0
        self.Circumference = 0

    def Accept(self):
        self.Radius = int(input("Enter radius : "))

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius**2)

    def CalculateCircumference(self):
        self.Circumference = 2*Circle.PI * self.Radius

    def Display(self):
        print("Radius of Circle :", self.Radius)
        print("Area of Circle :", self.Area)
        print("Circumference of Circle :", self.Circumference)

Obj = Circle()

Obj.Accept()
Obj.CalculateArea()
Obj.CalculateCircumference()
Obj.Display()
