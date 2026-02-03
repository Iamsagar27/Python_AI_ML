# 2. Design a Python application that creates two threads named EvenFactor and OddFactor.
# • Both threads should accept one integer number as a parameter.
# • The EvenFactor thread should:
# ◦ Identify all even factors of the given number.
# ◦ Calculate and display the sum of even factors.
# • The OddFactor thread should:
# ◦ Identify all odd factors of the given number.
# ◦ Calculate and display the sum of odd factors.
# • After both threads complete execution, the main thread should display the message: “Exit from main”

import threading

def Even(num):
    evenNumbers = []
    sum = 0
    while num != 0:
        fact = num % 10
        if(fact % 2 == 0):
            sum = sum + fact
            evenNumbers.append(fact)
        num //= 10

    print("-"*50)
    print("Even Numbers :", evenNumbers)
    print("Addition of Even Numbers :", sum)


def Odd(num):
    oddNumbers = []
    sum = 0
    while num != 0:
        fact = num % 10
        if(fact % 2 != 0):
            sum = sum + fact
            oddNumbers.append(fact)
        num //= 10

    print("-"*50)
    print("Odd Numbers :", oddNumbers)
    print("Addition of Odd Numbers :", sum)

def main():
    Number = int(input("Enter a number : "))

    EvenFactor = threading.Thread(target=Even, args=(Number,))
    OddFactor = threading.Thread(target=Odd, args=(Number,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("-"*50)
    print("Exit from main")

if __name__ == "__main__":
    main()