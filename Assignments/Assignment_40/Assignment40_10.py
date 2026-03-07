# 10. Train model with:
# max_depth = None
# Calculate:
# Training accuracy
# Testing accuracy
# If training accuracy is 100% but testing accuracy is lower, explain why this happens.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)

student_data = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
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
    max_depth=None,
    random_state=42
)

model.fit(X_train, Y_train)

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

training_accuracy = accuracy_score(Y_train, train_pred)
testing_accuracy = accuracy_score(Y_test, test_pred)

print("Training Accuracy :", training_accuracy * 100)
print("Testing Accuracy :", testing_accuracy * 100)
