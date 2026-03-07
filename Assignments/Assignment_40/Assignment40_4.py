# 4. Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their results.
# Display predictions clearly.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


# Load the dataset
file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)


# Decide Independent & Dependent variables
student_data = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = dataFrame[student_data]
Y = dataFrame["FinalResult"]


# Split the dataset for training and testing
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size = 0.3,
    random_state = 42
)


# Build the model
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)


# Train the model
model.fit(X_train, Y_train)


# Test the model
Y_Pred = model.predict(X_test)

new_students = pd.DataFrame({
    "StudyHours": [6, 4, 8, 3, 7],
    "Attendance": [85, 70, 95, 60, 90],
    "PreviousScore": [75, 65, 88, 50, 80],
    "AssignmentsCompleted": [8, 6, 10, 4, 9],
    "SleepHours": [7, 6, 8, 5, 7]
})

predictions = model.predict(new_students)

new_students["PredictedResult"] = predictions

print("\nPredictions for New Students:\n")
print(new_students)