# 4. Design a Python application that creates two threads.
# • Thread 1 should compute the sum of elements from a list.
# • Thread 2 should compute the product of elements from the same list.
# • Return the results to the main thread and display them.

import threading

def Sum(list):
    sum = 0

    for i in list:
        sum +=  i

    print("Sum of Numbers:", sum)


def Product(list):
    product = 1

    for i in list:
        product *= i

    print("Product of Numbers:", product)

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    Thread1 = threading.Thread(target=Sum, args=(numbers,))
    Thread2 = threading.Thread(target=Product, args=(numbers,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()