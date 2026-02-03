# 3. Design a Python application that creates two threads named EvenList and OddList.
# • Both threads should accept a list of integers as input.
# • The EvenList thread should:
# ◦ Extract all even elements from the list.
# ◦ Calculate and display their sum.
# • The OddList thread should:
# ◦ Extract all odd elements from the list.
# ◦ Calculate and display their sum.
# • Threads should run concurrently.

import threading

def Even(numbers):
    evenNumbers = []
    sum = 0
    
    for i in numbers:
        if(i % 2 == 0):
            sum += i
            evenNumbers.append(i)

    print("-"*50)
    print("Even Numbers :", evenNumbers)
    print("Addition of Even Numbers :", sum)


def Odd(numbers):
    oddNumbers = []
    sum = 0
    for i in numbers:
        if(i % 2 != 0):
            sum += i
            oddNumbers.append(i)

    print("-"*50)
    print("Odd Numbers :", oddNumbers)
    print("Addition of Odd Numbers :", sum)

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    EvenList = threading.Thread(target=Even, args=(numbers,))
    OddList = threading.Thread(target=Odd, args=(numbers,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

    print("-"*50)
    print("Exit from main")

if __name__ == "__main__":
    main()