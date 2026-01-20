# 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements

from functools import reduce

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    Addition = reduce(lambda x , y: x + y, numbers)

    print("Addition of elements :", Addition)

if __name__ == "__main__":
    main()