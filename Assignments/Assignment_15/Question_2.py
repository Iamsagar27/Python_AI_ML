# 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    Even = list(filter(lambda x : x % 2 == 0, numbers))

    print("List of even elements :", Even)

if __name__ == "__main__":
    main()