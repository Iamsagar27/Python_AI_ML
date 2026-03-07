# 1. Write a Python program to load the file student_performance_ml.csv using pandas. Display:
# First 5 records
# Last 5 records
# Total number of rows and columns
# List of column names
# Data types of each column

import pandas as pd

Border = "-"*100

file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)

# First 5 records
print(Border)
print("First 5 records :")
print(Border)
print(dataFrame.head())
print(Border+"\n")


# Last 5 records
print(Border)
print("Last 5 records :")
print(Border)
print(dataFrame.tail())
print(Border+"\n")

# Total number of rows and columns
print(Border)
print("Total number of rows and columns :")
print(Border)
print("Number of rows :", dataFrame.shape[0])
print("Number of columns :", len(list(dataFrame.columns)))
print(Border+"\n")


# List of column names
print(Border)
print("List of column names :")
print(Border)
print(list(dataFrame.columns))
print(Border+"\n")


# Data types of each column
print(Border)
print("Data types of each column :")
print(Border)
print(dataFrame.dtypes)
print(Border+"\n")