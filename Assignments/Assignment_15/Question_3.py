# 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    Odd = list(filter(lambda x : x % 2 == 1, numbers))

    print("List of odd elements :", Odd)

if __name__ == "__main__":
    main()