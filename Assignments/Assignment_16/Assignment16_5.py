# 5. 5.Write a program which display 10 to 1 on screen.
# Output : 10 9 8 7 6 5 4 3 2 1

def DisplayNumbers(num):
    numbers = ""

    for i in range(num,0,-1):
        numbers += str(i) + " "

    return numbers

def main():
    number = int(input("Enter a number : "))
       
    result = DisplayNumbers(number)
       
    print(result)

if __name__ == "__main__":
    main()
