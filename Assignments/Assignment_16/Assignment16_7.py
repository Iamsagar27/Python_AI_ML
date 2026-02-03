# 7. Write a program which contains one function that accept one number from user and returns true if number is 
# divisible by 5 otherwise return false.
# Input : 8 Output : False
# Input : 25 Output : True

def CheckNumber(num):
    if(num % 5 == 0):
         return True
    else :
         return False

def main():
    number = int(input("Enter a number : "))
       
    result = CheckNumber(number)
       
    print(result)

if __name__ == "__main__":
    main()
