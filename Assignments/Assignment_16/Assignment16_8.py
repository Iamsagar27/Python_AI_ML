# 8. Write a program which accept number from user and print that number of “*” on screen.
# Input : 5 
# Output : * * * * *

def PrintStar(num):
    stars = ""
    while num > 0:
        stars += "*" + " "
        num -= 1

    return stars

def main():
    number = int(input("Enter a number : "))
       
    result = PrintStar(number)
       
    print(result)

if __name__ == "__main__":
    main()
