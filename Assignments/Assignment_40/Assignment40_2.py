# 2. Remove the column SleepHours from the dataset.
# Train the model again.
# Compare new accuracy with previous accuracy.
# Does removing this feature affect performance?

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

# Load the dataset
file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)


# Decide Independent & Dependent variables
student_data = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted"
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


# Model Performance
accuracy = accuracy_score(Y_test, Y_Pred)

print("Accuracy : ", accuracy*100)
print("Removing SleepHours does not affect the performance accuracy")
