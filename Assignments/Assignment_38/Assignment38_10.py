# 10. Plot SleepHours againt FinalResult. Does Sleepin guarantees success? Explain.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)

pass_students = dataFrame[dataFrame["FinalResult"] == 1]
fail_students = dataFrame[dataFrame["FinalResult"] == 0]

plt.figure()

plt.scatter(pass_students["SleepHours"],pass_students["FinalResult"],label="Pass")

plt.scatter(fail_students["SleepHours"],fail_students["FinalResult"],label="Fail")

plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")
plt.title("Sleep Hours vs Final Result")
plt.legend()

plt.show()