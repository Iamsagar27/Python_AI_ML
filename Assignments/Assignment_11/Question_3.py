# 3. Write a program which accepts one number and prints sum of digits. 
# Input: 123 
# Output: 6 

def NumberCount(No):
    Sum = 0

    while No != 0:
        lastDigit = No % 10

        Sum += lastDigit
        
        No = No // 10
    
    return Sum


def main():
    Num = int(input("Enter a number :"))

    Ret = NumberCount(Num)

    print(Ret)

if __name__ == "__main__":
    main()