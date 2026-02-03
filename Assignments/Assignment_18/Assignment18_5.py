# 5. Write a program which accept N numbers from user and store it into List.
# Return addition of all prime numbers from that List. 
# Main python file accepts N numbers from user and pass each number to ChkPrime() function which is 
# part of our user defined module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 +2 + 5)

import MarvellousNum

def ListPrime(List):
    addition = 0

    for i in List:
        if(MarvellousNum.CheckPrime(i)):
            addition += i

    return addition

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    print("Enter the elements :")
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    print("Input Elements :", numbers)

    Result = ListPrime(numbers)
    print("Addition of prime numbers from the List :", Result)

if __name__ == "__main__":
    main()