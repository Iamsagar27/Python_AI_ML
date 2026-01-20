# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each numbers

def main():
    numbers = [2,3,4,5,6]

    Square = list(map(lambda x : x ** 2, numbers))

    print(Square)

if __name__ == "__main__":
    main()