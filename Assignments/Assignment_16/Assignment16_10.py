# 10. Write a program which accept name from user and display length of its name.
# Input : Marvellous 
# Output : 10

def StringLength(str):
    count = 0
    for i in str:
        count += 1
    return count

def main():
    string = input("Enter a name : ")
       
    result = StringLength(string)
       
    print(result)

if __name__ == "__main__":
    main()
