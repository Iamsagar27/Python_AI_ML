# 1. Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, 
# Mult() for multiplication and Div() for division. 
# All functions accepts two parameters as number and perform the operation. 
# Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

def ChkNum(num):
    if num % 2 == 0 :
        return "Even Number"
    else :
        return "Odd Number"

def main():
    try:
       number = int(input("Enter a number : "))
       
       result = ChkNum(number)
       
       print(result)
    
    except ValueError as vobj:
        print(vobj)

if __name__ == "__main__":
    main()