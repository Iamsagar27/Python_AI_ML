# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    Multiplication = reduce(lambda x, y: x * y  , numbers)

    print("Product of all elements :", Multiplication)

if __name__ == "__main__":
    main()