# 9. Create a new column:
# PerformanceIndex = (StudyHours * 2) + Attendance
# Train the model including this new feature.
# Does accuracy improve?

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)

dataFrame["PerformanceIndex"] = (dataFrame["StudyHours"] * 2) + dataFrame["Attendance"]

student_data = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    "PerformanceIndex"
]

X = dataFrame[student_data]
Y = dataFrame["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size = 0.5,
    random_state = 42
)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

model.fit(X_train, Y_train)

Y_Pred = model.predict(X_test)

accuracy = accuracy_score(Y_test, Y_Pred)

print("Accuracy :", accuracy * 100)
