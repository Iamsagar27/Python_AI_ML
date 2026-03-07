# 8. Create a boxplot for attendance. Identify if any outliners are present

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)

sns.boxplot(x = list(dataFrame["Attendance"]))
plt.show()