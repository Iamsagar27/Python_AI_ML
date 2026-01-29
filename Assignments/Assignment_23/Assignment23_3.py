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