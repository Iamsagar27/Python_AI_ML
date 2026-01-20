# 9. Write a lambda function which accepts two numbers and returns multiplication

def main():
    Num1 = int(input("Enter first number :"))
    Num2 = int(input("Enter second number :"))

    Multiplication = lambda x,y: x*y  

    print(Multiplication(Num1, Num2))

if __name__ == "__main__":
    main()