def EmployeeInfo(Name, Age, Salary, City="Pune"):
    print("Name :", Name)
    print("Age :", Age)
    print("Salary :", Salary)
    print("City :", City)

def main():
    EmployeeInfo(Age=26, Name="Rahul",Salary=2000.5)
    EmployeeInfo("Rahul",26 ,2000.5, "Pune")

if __name__ == "__main__":
    main()