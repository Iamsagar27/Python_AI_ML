# 4. Use value_counts () to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.


import pandas as pd

Border = "-"*100

file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)

print(Border)
print("Analysis of distribution of FinalResult : ")
print(dataFrame["FinalResult"].value_counts())


# Calculate the percentage of Pass and Fail students.
pass_count = 0
fail_count = 0
for i in dataFrame["FinalResult"]:
    if i == 1:
        pass_count += 1
    else :
        fail_count += 1

print()
print(Border)
print("Total number of student : ", dataFrame.shape[0])
print("Number of students passed : ", pass_count)
print("Number of students failed : ", fail_count)
print("Percentage of Students who Passed : ", pass_count/dataFrame.shape[0])
print("Percentage of Students who Failed : ", fail_count/dataFrame.shape[0] )
print(Border)

