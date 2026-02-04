# 3: Write a Python program to implement a class named Arithmetic with the following characteristics:
# The class should contain two instance variables: Valuel and Value2.
# Define a constructor (init) that initializes all instance variables to 0.
# Implement the following instance methods:
# Accept()accepts values for Valuel and Value2 from the user.
# Addition()returns the addition of Valuel and Value2.
# Subtraction ()returns the subtraction of Valuel and Value2.
# Multiplication()returns the multiplication of Valuel and Value2.
# Division()-returns the division of Valuel and Value2 (handle division by zero properly).
# Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithematic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number : ")) 
        self.Value2 = int(input("Enter second number : "))

    def Addition(self):
        addition = 0
        addition = self.Value1 + self.Value2
        print("Addition : ", addition)

    def Subtraction(self):
        subtraction = 0
        subtraction = self.Value1 - self.Value2
        print("Subtraction : ", subtraction)

    def Multiplication(self):
        multiplication = 0
        multiplication = self.Value1 * self.Value2
        print("Multiplication : ", multiplication)

    def Division(self):
        division = 0
        division = self.Value1 / self.Value2
        print("Division : ", division)

aObj = Arithematic()

aObj.Accept()
aObj.Addition()
aObj.Subtraction()
aObj.Multiplication()

aObj.Division()
