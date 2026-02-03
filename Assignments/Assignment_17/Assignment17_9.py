# 9. Write a program which accept number from user and return number of digits in that number.
# Input : 5187934 
# Output : 7

def NumberCount(num):
    count = 0

    while num != 0:
        num //= 10
        count += 1

    return count

def main():
    number = int(input("Enter a number : "))

    result= NumberCount(number)

    print(result)

if __name__ == "__main__":
    main()
