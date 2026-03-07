# 6. Plot a histogram of StudyHours. Explain what the distribution telss you

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)

sns.histplot(data = list(dataFrame["StudyHours"]))
plt.show()