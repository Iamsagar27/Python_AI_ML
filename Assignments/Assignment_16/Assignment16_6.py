# 6. Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input : 11 Output : Positive Number
# Input : -8 Output : Negative Number
# Input : 0 Output : Zero

def CheckNumber(num):
    if(num > 0):
         return "Positive Number"
    elif (num < 0):
         return "Negative Number"
    else :
         return "Zero"

def main():
    number = int(input("Enter a number : "))
       
    result = CheckNumber(number)
       
    print(result)

if __name__ == "__main__":
    main()
