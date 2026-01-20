# 5. Write a program which accepts one number and checks whether it is palindrome or not. 
# Input: 121 
# Output: Palindrome 

def ReverseNumber(No):
    reverseNumber = 0

    while No > 0: # 754
        lastDigit = No % 10  # 754 % 10 = 4
        
        reverseNumber = reverseNumber * 10 + lastDigit # 0 * 10 + 4 = 4
        
        No = No // 10    # 754 // 10 = 75

    return reverseNumber

def main():
    Num = int(input("Enter a number :"))

    Ret = ReverseNumber(Num)

    if(Ret == Num):
        print("Palindrome")
    else :
        print("Not Palindrome")

if __name__ == "__main__":
    main()