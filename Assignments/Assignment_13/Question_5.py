# 5. Write a program which accepts marks and displays grade. 
# Condition Example: 
# ≥ 75 → Distinction 
# ≥ 60 → First Class 
# ≥ 50 → Second Class 
# <50 → Fail 

def DisplayGrade(marks):
    if(marks >= 75):
        return "Distinction"
    elif(marks >= 60):
        return "First Class"
    elif(marks >= 50):
        return "Second Class"
    elif(marks < 50):
        return "Fail"

def main():
    marks = int(input("Enter the marks:"))

    Result = DisplayGrade(marks)

    print(Result)

if __name__ == "__main__":
    main()