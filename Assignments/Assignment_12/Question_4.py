# 4. Write a program which accepts one number and prints that many numbers starting from 1. 
# Input: 5 
# Output: 1 2 3 4 5 

def AscendingNumbers(No):
    numbers = ""
    for i in range(1, No+1):
        numbers += str(i) + " "
    return numbers

def main():
    Num = int(input("Enter a number :"))

    Result = AscendingNumbers(Num)

    print(Result)

if __name__ == "__main__":
    main()