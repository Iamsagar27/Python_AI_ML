# 8. Write a program which accept one number and display below pattern.
# Input : 5
# Output :  1
#           1 2
#           1 2 3
#           1 2 3 4
#           1 2 3 4 5

def PrintNumbers(num):
    numbers = ""
    for i in range(1,num+1):
        for j in range(1,i+1):
            numbers += str(j) + " "
        numbers += "\n"
        num -= 1
    return numbers

def main():
    number = int(input("Enter a number : "))

    result= PrintNumbers(number)

    print(result)

if __name__ == "__main__":
    main()
