# 1. Write a program which accepts length and width of rectangle and prints area. 

def AreaOfRectangle(l, w):
    Area = 0
    Area = l * w
    return Area

def main():
    Length = int(input("Enter the length:"))
    Width = int(input("Enter the width:"))

    Result = AreaOfRectangle(Length, Width)

    print("Area of rectangle : ", Result)

if __name__ == "__main__":
    main()
