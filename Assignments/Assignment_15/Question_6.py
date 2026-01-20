# 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum elements

from functools import reduce

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    Minimum = reduce(lambda x , y: x if x < y else y, numbers)

    print("Minimum of elements :", Minimum)

if __name__ == "__main__":
    main()