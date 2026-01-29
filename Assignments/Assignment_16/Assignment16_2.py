# 2. Write a program which contains one function named as ChkNum() which accept one parameter as number. 
# If number is even then it should display “Even number” otherwise display “Odd number” on console.
# Input : 11 Output : Odd Number
# Input : 8 Output : Even Number

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