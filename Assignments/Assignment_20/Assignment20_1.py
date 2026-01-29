# 1. Design a Python application that creates two separate threads named Even and Odd.
# • The Even thread should display the first 10 even numbers.
# • The Odd thread should display the first 10 odd numbers.
# • Both threads should execute independently using the threading module.
# • Ensure proper thread creation and execution.

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