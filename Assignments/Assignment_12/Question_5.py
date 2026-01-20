# 5. Write a program which accepts one number and prints that many numbers in reverse order. 
# Input: 5 
# Output: 54321

def DescendingNumbers(No):
    numbers = ""
    for i in range(No, 0, -1):
        numbers += str(i) + " "
    return numbers

def main():
    Num = int(input("Enter a number :"))

    Result = DescendingNumbers(Num)

    print(Result)

if __name__ == "__main__":
    main()