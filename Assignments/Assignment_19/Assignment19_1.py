# 1. Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input : 4 Output : 16
# Input : 6 Output : 64

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