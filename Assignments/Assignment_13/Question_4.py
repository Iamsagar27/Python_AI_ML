# 4. Write a program which accepts one number and prints binary equivalent. 

def BinaryValue(No):
    if(No == 0):
        return 0
    
    space = ""

    temp = No   
    while temp > 0:
        remainder = temp % 2

        space = str(remainder) + space

        temp //= 2

    return space

def main():
    Number = int(input("Enter the Number :"))

    Result = BinaryValue(Number)

    print("Binary Value : ", Result)

if __name__ == "__main__":
    main()
