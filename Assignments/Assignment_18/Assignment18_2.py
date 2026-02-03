# 2. Write a program which accept N numbers from user and store it into List.
# Return Maximum number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

from functools import reduce

# def MaximumNumber1(numbers):
#     max = numbers[0]
#     for i in numbers:
#         if(i > max):
#             max = i
#     return max

def MaximumNumber(A,B):
    if A > B:
        return A
    else :
        return B

def main():

    numbers = []

    NumList = int(input("Enter number of elements : "))
    print("Enter the elements :")
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)
    
    Result = reduce(MaximumNumber, numbers)
    #Result1 = MaximumNumber1(numbers)
       
    print("Maximum number from list : ",Result)
    #print("Maximum number from list : ",Result1)

if __name__ == "__main__":
    main()