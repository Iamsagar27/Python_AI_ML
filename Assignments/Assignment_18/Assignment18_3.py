# 3. Write a program which accept N numbers from user and store it into List.
# Return Minimum number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5

from functools import reduce

#def MinimumNumber1(numbers):
#    min = numbers[0]
#    for i in numbers:
#        if(i < min):
#            min = i
#    return min

def MinimumNumber(A,B):
    if A < B:
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
    
    Result = reduce(MinimumNumber, numbers)
    #Result1 = MinimumNumber1(numbers)
       
    print("Minimum number from list : ",Result)
    #print("Minimum number from list : ",Result1)

if __name__ == "__main__":
    main()