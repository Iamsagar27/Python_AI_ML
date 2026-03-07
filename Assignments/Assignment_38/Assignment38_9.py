# 9. Create plot to show the relationship between AssignmentsCompleted and FinalResult. Explain your observation.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)

pass_students = dataFrame[dataFrame["FinalResult"] == 1]
fail_students = dataFrame[dataFrame["FinalResult"] == 0]

plt.figure()

plt.scatter(pass_students["AssignmentsCompleted"],pass_students["FinalResult"],label="Pass")

plt.scatter(fail_students["AssignmentsCompleted"],fail_students["FinalResult"],label="Fail")

plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")
plt.title("Assignments Completed vs Final Result")
plt.legend()

plt.show()