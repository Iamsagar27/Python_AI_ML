# 2: Write a Python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables:
# Name (Account holder name)
# Amount (Account balance)
# The class should contain one class variable:
# ROI (Rate of Interest), initialized to 10.5
# Define a constructor (init) that accepts Name and initial Amount.
# Implement the following instance methods:
# Display()-displays account holder name and current balance
# Deposit() accepts an amount from the user and adds it to balance.
# Withdraw() accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
# CalculateInterest() calculates and returns interest using formula:
# Interest = (Amount ROI) / 100
# Create multiple objects and demonstrate all methods.

class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter Name : ")
        self.Amount = int(input("Enter Bank Balance : "))
        print("-"*50)

    def Display(self):
        print("Name :", self.Name)
        print("Account Balance :", self.Amount)
        print("-"*50)

    def Deposit(self):
        self.NewAmount = int(input("Enter the amount :"))
        self.Amount += self.NewAmount
        print("Account Balance after Deposit :", self.Amount)
        print("-"*50)

    def Withdraw(self):
        self.NewAmount = int(input("Enter the amount :"))
        if self.Amount > self.NewAmount:
            self.Amount -= self.NewAmount
            print("Account Balance after Withdraw :", self.Amount)
            print("-"*50)
        else:
            print("Insufficient Balance. Current Balance :", self.Amount)
            print("-"*50)

    def CalculateInterest(self):
        self.Interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest :", self.Interest)

Obj = BankAccount()

Obj.Display()
Obj.Deposit()
Obj.Withdraw()
Obj.CalculateInterest()


