# 1. Design a Python application that creates two threads named Prime and NonPrime.
# • Both threads should accept a list of integers.
# • The Prime thread should display all prime numbers from the list.
# • The NonPrime thread should display all non-prime numbers from the list.

import threading

def Prime(list):
    primenumbers = ""

    for i in list:
        if i > 1:
            count = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    count += 1

            if count == 2:
                primenumbers += str(i) + " "

    print("Prime Numbers:", primenumbers)


def NonPrime(list):
    nonprimenumbers = ""

    for i in list:
        if i > 1:
            count = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    count += 1

            if count > 2:
                nonprimenumbers += str(i) + " "

    print("Non-Prime Numbers :", nonprimenumbers)

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    Thread1 = threading.Thread(target=Prime, args=(numbers,))
    Thread2 = threading.Thread(target=NonPrime, args=(numbers,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()