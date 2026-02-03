# 4. Write a program which accept N numbers from user and store it into List.
# Accept one another number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def SearchElement(element, elements):
    count = 0

    for i in elements:
        if(i == element):
            count += 1
    return count

def main():

    numbers = []

    NumList = int(input("Enter number of elements : "))
    print("Enter the elements :")
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)
    
    print("Input Elements :", numbers)

    search = int(input("Element to search : "))
    Result = SearchElement(search, numbers)
    print("Element Count :", Result)

if __name__ == "__main__":
    main()