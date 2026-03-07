# 3. Using pandas functions, calculate and display:
# Average StudyHours
# Average Attendance
# Maximum Previous Score
# Minimum SleepHours

import pandas as pd

Border = "-"*100

file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)


# Average StudyHours
sum = 0
print(Border)

for i in dataFrame["StudyHours"]:
    sum += i

avg = sum/dataFrame.shape[0]
print("Average StudyHours : ", avg)


# Average Attendance
sum = 0

for i in dataFrame["Attendance"]:
    sum += i

avg = sum/dataFrame.shape[0]
print("Average Attendance : ", avg)


# Maximum Previous Score
max = 0

for i in dataFrame["PreviousScore"]:
    if i > max:
        max = i

print("Maximum Previous Score : ", max)


# Minimum SleepHours
min = dataFrame["SleepHours"][0]
for i in dataFrame["SleepHours"]:
    if i < min:
        min = i


print("Minimum SleepHours : ", min)
print(Border+"\n")