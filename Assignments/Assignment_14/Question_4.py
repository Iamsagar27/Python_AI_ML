# 4. Write a lambda function which accepts two numbers and returns minimum number 

def main():
    Num1 = int(input("Enter first number :"))
    Num2 = int(input("Enter second number :"))

    Minimum = lambda x, y : x if x < y else y 

    print(Minimum(Num1, Num2))

if __name__ == "__main__":
    main()