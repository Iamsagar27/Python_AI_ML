# 10. Write a program which accept number from user and return addition ofdigits in that number.
# Input : 5187934 
# Output : 37

def NumberCount(num):
    addition = 0

    while num != 0:
        last = num % 10
        addition = addition + last 
        num //= 10

    return addition

def main():
    number = int(input("Enter a number : "))

    result= NumberCount(number)

    print(result)

if __name__ == "__main__":
    main()
