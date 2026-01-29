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