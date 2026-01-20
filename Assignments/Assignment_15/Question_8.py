# 8. Write a lambda function using filter () which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    Divisible = list(filter(lambda x : (x % 3 == 0 and x % 5 == 0) , numbers))

    print("Numbers divisible by 3 and 5 :", Divisible)

if __name__ == "__main__":
    main()