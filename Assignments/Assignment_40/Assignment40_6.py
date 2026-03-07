# 6. Identify students where:
# y_test != y_pred
# . Display those rows.
# How many students were misclassified?
# What common pattern do you observe?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
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
    max_depth=5,
    random_state=42
)

model.fit(X_train, Y_train)

Y_Pred = model.predict(X_test)

misclassified = X_test[Y_test != Y_Pred]

print("\nMisclassified Students:\n")
print(misclassified)

misclassified_count = (Y_test != Y_Pred).sum()

print("\nNumber of Misclassified Students:", misclassified_count)