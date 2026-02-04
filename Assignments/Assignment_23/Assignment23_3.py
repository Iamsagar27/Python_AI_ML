# 3: Write a Python program to implement a class named Numbers with the following specifications:
# The class should contain one instance variable:
# Value
# Define a constructor (init) that accepts a number from the user and initializes Value.
# Implement the following instance methods:
# ChkPrime()returns True if the number is prime, otherwise returns False
# ChkPerfect()-returns True if the number is perfect, otherwise returns False
# Factors()-displays all factors of the number
# SumFactors()-returns the sum of all factors
# (You may use this method as a helper in ChkPerfect() if required)
# Create multiple objects and call all methods.

class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number : "))

    def ChkPrime(self):
        self.count = 0
        for i in range(1, self.Value+1):
            if self.Value % i == 0:
                self.count += 1

        if self.count == 2:
            return True
        else :
            return False

    def ChkPerfect(self):
        self.count = 0
        self.sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                self.sum += i

        if self.sum == self.Value:
            return True
        else :
            return False

Obj = Numbers()

Obj.ChkPrime()
print(Obj.ChkPrime())

Obj.ChkPerfect()

print(Obj.ChkPerfect())
