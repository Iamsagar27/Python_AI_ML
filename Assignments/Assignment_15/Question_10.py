# 10. Write a lambda function using filter () which accepts a list of numbers and returns the count of even numbers. 

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    EvenCnt = list(filter(lambda x: x % 2 == 0 , numbers))

    print("No. of even elements :", len(EvenCnt))

if __name__ == "__main__":
    main()