# 3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division. 

def Addition(No1, No2):
    Addition = No1 + No2
    return Addition

def Subtraction(No1, No2):
    Addition = No1 - No2
    return Addition

def Multiplication(No1, No2):
    Addition = No1 * No2
    return Addition

def Division(No1, No2):
    Addition = No1 / No2
    return Addition

def main():
    Num1 = int(input("Enter first number :"))
    Num2 = int(input("Enter first number :"))

    aResult = Addition(Num1, Num2)
    sResult = Subtraction(Num1, Num2)
    mResult = Multiplication(Num1, Num2)
    dResult = Division(Num1, Num2)

    print("Addition :", aResult)
    print("Subtraction :", sResult)
    print("Multiplication :", mResult)
    print("Division :", dResult)

if __name__ == "__main__":
    main()