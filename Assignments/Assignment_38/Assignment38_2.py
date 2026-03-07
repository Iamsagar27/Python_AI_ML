# 2. Write a program to:
# Display total number of students in the dataset
# Count how many students Passed (FinalResult = 1)
# Count how many students Failed (FinalResult = 0)

import pandas as pd

Border = "-"*100

file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)

# Display total number of students in the dataset
print(Border)
print("Total number of students in the dataset : ", dataFrame.shape[0])

# Count how many students Passed (FinalResult = 1)
count = 0
for i in dataFrame["FinalResult"] :
    if i == 1:
        count += 1
print("Count how many students Passed (FinalResult = 1) :", count)

# Count how many students Failed (FinalResult = 0)
count = 0
for i in dataFrame["FinalResult"] :
    if i == 0:
        count += 1
print("Count how many students Failed (FinalResult = 0) :", count)
print(Border+"\n")