# 2. Write a program which accept one number and display below pattern.
# Input : 5
# Output :  * * * * *
#           * * * * *
#           * * * * *
#           * * * * *
#           * * * * *

def PrintStars(num):
    stars = ""
    for i in range(num):
        for j in range(num):
            stars += "*" + " "
        stars += "\n"
    return stars

def main():
    number = int(input("Enter a number : "))

    result= PrintStars(number)

    print(result)

if __name__ == "__main__":
    main()
