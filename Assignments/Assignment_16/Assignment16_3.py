# 3. Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
# Input : 11 5 
# Output : 16

def Add(num1,num2):
    Addition = 0
    Addition = num1 + num2
    return Addition
    
def main():
    try:
       number1 = int(input("Enter first number : "))
       number2 = int(input("Enter second number : "))
       
       result = Add(number1,number2)
       
       print("Addition of 2 numbers :", result)
    
    except ValueError as vobj:
        print(vobj)

if __name__ == "__main__":
    main()