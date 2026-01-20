# 7. Write a lambda function using filter() which accepts a list of strings and returns a list of string having length greater than 5

def main():
    strings = []

    stringList = int(input("Enter number of elements : "))
    for i in range(stringList):
        elements = input()
        strings.append(elements)

    StringLength = list(filter(lambda x : len(x) > 5 , strings))

    print("List of string having length greater than 5 :", StringLength)

if __name__ == "__main__":
    main()