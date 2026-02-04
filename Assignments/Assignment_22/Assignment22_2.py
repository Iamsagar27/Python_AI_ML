# 2: Write a Python program to implement a class named Circle with the following requirements:
# The class should contain three instance variables: Radius, Area. and Circumference.
# The class should contain one class variable named PI, initialized to 3.14.
# Define a constructor (init) that initializes all instance variables to 0.0.
# Implement the following instance methods:
# Accept()accepts the radius of the circle from the user.
# CalculateArea() calculates the area of the circle and stores it in the Area variable.
# CalculateCircumference() calculates the circumference of the circle and stores it in the Circumference variable.
# Display()-displays the values of Radius, Area, and Circumference.
# Create multiple objects of the Circle class and invoke all the instance methods for each object.

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

