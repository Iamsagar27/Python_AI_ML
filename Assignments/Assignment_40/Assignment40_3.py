# 3. Train the model using only:
# StudyHours
# Attendance
# Compare the accuracy with the full-feature model. Is the model still performing well?


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)

full_student_data = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = dataFrame[full_student_data]
Y = dataFrame["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size = 0.5,
    random_state = 42
)

full_model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

full_model.fit(X_train, Y_train)

Y_Pred = full_model.predict(X_test)

full_accuracy = accuracy_score(Y_test, Y_Pred)

print("Accuracy using ALL features:", full_accuracy * 100)


limited_student_data = [
    "StudyHours",
    "Attendance"
]

X = dataFrame[limited_student_data]
Y = dataFrame["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size = 0.5,
    random_state = 42
)

limited_model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

limited_model.fit(X_train, Y_train)

Y_Pred = limited_model.predict(X_test)

limited_accuracy = accuracy_score(Y_test, Y_Pred)

print("Accuracy using StudyHour and Attendance features:", limited_accuracy * 100)
print("Accuracy Difference:", (full_accuracy - limited_accuracy) * 100)