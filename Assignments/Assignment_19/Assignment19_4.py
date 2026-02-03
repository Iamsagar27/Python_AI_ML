# 4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. 
# Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204


from functools import reduce

#filterList = lambda x : x if x % 2 == 0 else None 
def filterList(num):
    if(num % 2 == 0):
        return num
        
#mapList = lambda x : x**2
def mapList(num):
    return num**2

#reduceList = lambda x,y : x+y
def reduceList(num1,num2):
    return num1 + num2

def main():
    numbers = []

    NumList = int(input("Enter number of elements : "))
    for i in range(NumList):
        elements = int(input())
        numbers.append(elements)

    print("Input List :", numbers)

    filterNumbers = list(filter(filterList, numbers))
    print("List after filter :", filterNumbers)

    mapNumbers = list(map(mapList, filterNumbers))
    print("List after map :", mapNumbers)

    reduceNumbers = reduce(reduceList, mapNumbers)
    print("Output of reduce :", reduceNumbers)

if __name__ == "__main__":
    main()