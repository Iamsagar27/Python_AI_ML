# 5. Write a program which accept one number for user and check whether number is prime or not.
# Input : 5 
# Output : It is Prime Number

def PrimeNumber(num):
    count = 0
    for i in range(1,num+1):
        if(num % i == 0):
            count += 1

    if(count == 2):
        return "It is Prime Number"
    else :
        return "It is not Prime Number"


def main():
    number = int(input("Enter a number : "))

    result= PrimeNumber(number)

    print(result)

if __name__ == "__main__":
    main()
