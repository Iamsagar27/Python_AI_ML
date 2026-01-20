# 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum elements

from functools import reduce

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    Maximum = reduce(lambda x , y: x if x > y else y, numbers)

    print("Maximum of elements :", Maximum)

if __name__ == "__main__":
    main()