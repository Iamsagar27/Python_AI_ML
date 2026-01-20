# 4. Write a program which accepts one number and prints reverse of that number. 
# Input: 123 
# Output: 321 

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

    print(Ret)

if __name__ == "__main__":
    main()