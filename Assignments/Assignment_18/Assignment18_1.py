# 1. Write a program which accept N numbers from user and store it into List.
# Return addition of all elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

def ChkNum(num):
    if num % 2 == 0 :
        return "Even Number"
    else :
        return "Odd Number"

def main():
    try:
       number = int(input("Enter a number : "))
       
       result = ChkNum(number)
       
       print(result)
    
    except ValueError as vobj:
        print(vobj)

if __name__ == "__main__":
    main()