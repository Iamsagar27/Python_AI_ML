# 2. 2.Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input : 4 3 Output : 12
# Input : 6 3 Output : 18

Multiplication = lambda x,y : x*y

def main():
    number1 = int(input("Enter first number : "))
    number2 = int(input("Enter second number : "))
    result = Multiplication(number1,number2) 
    print(result)

if __name__ == "__main__":
    main()