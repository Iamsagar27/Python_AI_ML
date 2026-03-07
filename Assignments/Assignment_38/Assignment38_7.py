# 7. Create a scatter plot of  StudyHours vs PreviousScore

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)

pass_student = dataFrame[dataFrame["FinalResult"] == 1]
fail_student = dataFrame[dataFrame["FinalResult"] == 0]

plt.figure()

plt.scatter(pass_student["StudyHours"], pass_student["PreviousScore"], label = "Pass")
plt.scatter(fail_student["StudyHours"], fail_student["PreviousScore"], label = "Fail")

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours vs Previous Score")
plt.legend()
plt.show()