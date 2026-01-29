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

