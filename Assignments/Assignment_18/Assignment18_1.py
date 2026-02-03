# 1. Write a program which accept N numbers from user and store it into List.
# Return addition of all elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

from functools import reduce

def AdditionList(A,B):
    return A+B

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    print("Enter the elements :")
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)
    
    Result = reduce(AdditionList, numbers)
       
    print(Result)

if __name__ == "__main__":
    main()