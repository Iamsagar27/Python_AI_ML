# 7. Train model using:
# random_state = 0
# random_state = 10
# random_state = 42
# Compare testing accuracy.
# Does the result change?

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

random_states = [0,10,42]

for i in random_states:

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size = 0.5,
        random_state = i
    )

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=5,
        random_state=42
    )

    model.fit(X_train, Y_train)

    Y_Pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_Pred)

    print("Random State:", i)
    print("Testing Accuracy:", accuracy * 100)

print("Accuracy does not change even if the value of random_state changes")