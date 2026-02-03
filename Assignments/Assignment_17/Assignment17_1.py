# 1. Create on module named as Arithmetic which contains 4 functions as Add() for addition, 
# Sub() for subtraction, Mult() for multiplication and Div() for division. 
# All functions accepts two parameters as number and perform the operation. 
# Write on python program which call all the functions from Arithmetic module by accepting 
# the parameters from user.

import Arithmetic

def main():
    number1 = int(input("Enter first number : "))
    number2 = int(input("Enter second number : "))
       
    Addition = Arithmetic.Addition(number1,number2)
    Subtraction = Arithmetic.Subtraction(number1,number2)
    Multiplication = Arithmetic.Multiplication(number1,number2)
    Division = Arithmetic.Division(number1,number2)
       
    print("Addition : ", Addition)
    print("Subtraction : ", Subtraction)
    print("Multiplication : ", Multiplication)
    print("Division : ", Division)

if __name__ == "__main__":
    main()
