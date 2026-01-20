# 8. Write a lambda function which accepts two numbers and returns addition

def main():
    Num1 = int(input("Enter first number :"))
    Num2 = int(input("Enter second number :"))

    Addition = lambda x,y: x+y  

    print(Addition(Num1, Num2))

if __name__ == "__main__":
    main()